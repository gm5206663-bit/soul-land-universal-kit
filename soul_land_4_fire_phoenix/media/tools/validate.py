#!/usr/bin/env python3
"""Technical/integrity checks, not a guarantee of artistic or canonical fidelity."""
from pathlib import Path
import argparse,json,hashlib,subprocess,re,datetime
from PIL import Image
import numpy as np
import imageio_ffmpeg
ROOT=Path(__file__).resolve().parents[1]
FF=imageio_ffmpeg.get_ffmpeg_exe()

def probe(path):
    r=subprocess.run([FF,'-hide_banner','-i',str(path)],capture_output=True,text=True)
    text=r.stderr
    m=re.search(r'Duration: (\d+):(\d+):(\d+\.\d+)',text)
    if not m:raise RuntimeError(f'No duration for {path.name}: {text[:300]}')
    return int(m[1])*3600+int(m[2])*60+float(m[3]),text

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source',type=Path,required=True);ap.add_argument('--check-manifest',action='store_true');ap.add_argument('--no-write',action='store_true');a=ap.parse_args()
    checks=[];videos=[];audios=[]
    def check(name,condition,detail):
        checks.append(dict(check=name,passed=bool(condition),detail=detail))
        if not condition:raise AssertionError(name+': '+str(detail))
    data=json.loads((ROOT/'metadata/chapters.json').read_text());chs=data['chapters']
    project=a.source/'soul_land_4_fire_phoenix'
    state=json.loads((project/'foundation/CURRENT_STATE_MANIFEST.json').read_text())
    check('published edge',state['latest_fic_chapter']==52,state['latest_fic_chapter'])
    check('chapter sequence',[c['number'] for c in chs]==list(range(1,53)),'1–52 once each')
    for ch in chs:
        check(f'source SHA256 {ch["number"]:02d}',hashlib.sha256((project/ch['source']).read_bytes()).hexdigest()==ch['sha256'],ch['source'])
    art=[x for x in chs if x['art']]
    check('illustration coverage',len(art)==10 and len({x['art'] for x in art})==8,{'chapter_entries':len(art),'unique_keyframes':len({x['art'] for x in art})})
    plates=list((ROOT/'cards').glob('chapter-*.jpg'));check('chapter plates',len(plates)==52,len(plates))
    images=list((ROOT/'assets').glob('*'))+list((ROOT/'cards').glob('*.jpg'))+[ROOT/'POSTER.jpg']
    for p in images:
        with Image.open(p) as im:im.verify()
    check('image integrity',True,f'{len(images)} images decoded')
    for p in plates:
        with Image.open(p) as im:check(f'plate size {p.stem}',im.size==(1280,720),im.size)
    scripts=list((ROOT/'audio').glob('*-script.txt'));mp3=list((ROOT/'audio').glob('*.mp3'))
    check('narration inventory',len(scripts)==len(mp3)==10,{'scripts':len(scripts),'mp3':len(mp3)})
    for p in sorted(mp3):
        raw=subprocess.run([FF,'-v','error','-i',str(p),'-f','f32le','-ar','16000','-ac','1','pipe:1'],check=True,capture_output=True).stdout
        samples=np.frombuffer(raw,dtype='<f4');duration=len(samples)/16000
        peak=float(np.max(np.abs(samples)));rms=float(np.sqrt(np.mean(samples**2)))
        check(f'audio signal {p.name}',duration>10 and np.isfinite(samples).all() and rms>.005,dict(seconds=round(duration,3),peak=round(peak,4),rms=round(rms,4)))
        audios.append(dict(file=str(p.relative_to(ROOT)),seconds=round(duration,3),peak=round(peak,4)))
    for p in sorted((ROOT/'video').glob('*.mp4')):
        duration,text=probe(p)
        check('video streams '+p.name,'h264' in text and 'aac' in text and '1280x720' in text,{'seconds':duration,'bytes':p.stat().st_size})
        subprocess.run([FF,'-v','error','-threads','2','-i',str(p),'-map','0:v:0','-map','0:a:0','-f','null','-'],check=True,capture_output=True,timeout=150)
        check('full video/audio decode '+p.name,True,'All frames and audio decoded without ffmpeg errors')
        videos.append(dict(file=str(p.relative_to(ROOT)),seconds=duration,bytes=p.stat().st_size))
    check('video count',len(videos)==2,len(videos))
    vtts=list((ROOT/'video').glob('*.vtt'));check('caption sidecars',len(vtts)==2,len(vtts))
    for p in vtts:check('caption header '+p.name,p.read_text().startswith('WEBVTT'),'Estimated timing explicitly marked')
    gallery=(ROOT/'index.html').read_text()
    check('gallery chapter inventory',gallery.count('class="chapter"')==52,gallery.count('class="chapter"'))
    check('gallery embedded images','data:image/jpeg;base64,' in gallery and 'https://fonts.' not in gallery,'No external image/font dependency for offline gallery art')
    check('rights disclosure',all('non-commercial' in (ROOT/p).read_text() for p in ['README.md','CREDITS.md']),'Disclaimer present in both primary documents')
    if a.check_manifest:
        manifest=json.loads((ROOT/'metadata/checksums.json').read_text())['files']
        for rel,info in manifest.items():check('manifest '+rel,hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==info['sha256'],info['sha256'])
        actual={str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='checksums.json'}
        check('manifest complete',actual==set(manifest),'Every deliverable except the manifest itself is hashed')
    report=dict(passed=True,coverage='Technical integrity only; see QA.md for unresolved creative work',source_revision=data['source_revision'],source_chapters_unchanged=52,checks=checks,videos=videos,audios=audios)
    if not a.no_write:(ROOT/'metadata/validation.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(passed=True,checks=len(checks),videos=videos,audio_tracks=len(audios)),indent=2))

if __name__=='__main__':main()
