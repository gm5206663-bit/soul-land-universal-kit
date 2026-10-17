#!/usr/bin/env python3
"""Render chapter plates and narrated motion storyboards from reviewed assets.

No character-animation claim: this uses slow camera moves on illustrations and
chapter plates. Narration chapter transitions are estimated, not forced-aligned.
"""
from pathlib import Path
import json,math,re,subprocess,concurrent.futures,argparse,hashlib
import numpy as np
from PIL import Image,ImageOps,ImageDraw,ImageFont,ImageFilter
import imageio_ffmpeg

ROOT=Path(__file__).resolve().parents[1]
FF=imageio_ffmpeg.get_ffmpeg_exe()
W,H=1280,720
FPS=24
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
SERIF='/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'
GOLD=(241,193,115);WHITE=(244,241,232);DIM=(173,180,190)


def font(size,style=FONT):return ImageFont.truetype(style,size)

def wrap(text,draw,f,maxwidth):
    result=[];line=''
    for word in text.split():
        attempt=(line+' '+word).strip()
        if draw.textlength(attempt,font=f)>maxwidth and line:result.append(line);line=word
        else:line=attempt
    if line:result.append(line)
    return result


def cover(path,size=(W,H)):
    return ImageOps.fit(Image.open(path).convert('RGB'),size,centering=(.5,.42))


def abstract(number):
    yy,xx=np.mgrid[0:H,0:W]
    glow=np.exp(-((xx-W*.77)**2/(W*.25)**2+(yy-H*.35)**2/(H*.6)**2))
    a=np.zeros((H,W,3),dtype=np.uint8)
    a[:,:,0]=10+glow*31;a[:,:,1]=17+glow*15;a[:,:,2]=26+glow*10
    im=Image.fromarray(a);d=ImageDraw.Draw(im)
    # Abstract feather geometry, not an in-world martial-soul depiction.
    for i in range(19):
        x=800+i*15;y=120+i*16
        d.arc((x-160,y-100,x+180,y+180),180,285,fill=(72+i*2,61+i,53),width=2)
    d.text((940,390),f'{number:02d}',font=font(190,BOLD),fill=(35,42,52))
    return im


def plate(ch):
    im=cover(ROOT/'assets'/ch['art']) if ch['art'] else abstract(ch['number'])
    im=im.convert('RGBA')
    shade=Image.new('RGBA',(W,H));p=shade.load()
    # Protect readable titles and avoid hiding the character on the right.
    for x in range(W):
        alpha=int(218*(1-x/W)**.7+30)
        for y in range(H):p[x,y]=(5,10,17,min(alpha+int(35*y/H),245))
    im=Image.alpha_composite(im,shade)
    d=ImageDraw.Draw(im)
    d.line((68,70,118,70),fill=GOLD,width=3)
    d.text((136,58),'FIRE PHOENIX  /  PUBLISHED CHRONICLE',font=font(15,BOLD),fill=GOLD)
    d.text((68,139),f'CHAPTER {ch["number"]:02d}',font=font(18,BOLD),fill=DIM)
    titlelines=wrap(ch['title'],d,font(47,SERIF),760)
    y=184
    for line in titlelines:d.text((65,y),line,font=font(47,SERIF),fill=WHITE);y+=60
    y+=25
    for line in wrap(ch['beat'],d,font(25),795):d.text((68,y),line,font=font(25),fill=WHITE);y+=37
    if ch['number'] in (46,47):
        d.text((68,548),'#1 DORM 333 · 20,341     #2 DORM 336 · 9,846',font=font(19,BOLD),fill=GOLD)
    tag='ILLUSTRATED ARC KEYFRAME' if ch['art'] else 'STORYBOARD PLATE / SCENE ART PLANNED'
    d.text((68,601),tag,font=font(14,BOLD),fill=GOLD)
    d.text((68,635),'AI-generated fan visuals  •  Not official animation  •  Spoilers through Chapter 52',font=font(13),fill=DIM)
    d.line((68,679,1212,679),fill=(63,69,77),width=2)
    d.line((68,679,68+int(1144*ch['number']/52),679),fill=GOLD,width=3)
    return im.convert('RGB')


def poster(title,subtitle,art,small='NON-COMMERCIAL FAN WORK · GAURAV MEENA'):
    im=cover(ROOT/'assets'/art).convert('RGBA')
    grad=Image.new('RGBA',(W,H));d=ImageDraw.Draw(grad)
    for x in range(W):d.line((x,0,x,H),fill=(4,10,17,int(225*(1-x/W)**1.2+18)))
    im=Image.alpha_composite(im,grad);d=ImageDraw.Draw(im)
    d.text((65,75),'A SOUL LAND 4 FAN PROJECT',font=font(15,BOLD),fill=GOLD)
    for i,line in enumerate(title.split('\n')):d.text((60,174+i*89),line,font=font(77,SERIF),fill=WHITE)
    yy=174+len(title.split('\n'))*89+30
    for line in wrap(subtitle,d,font(24),670):d.text((67,yy),line,font=font(24),fill=WHITE);yy+=37
    d.text((67,650),small,font=font(13,BOLD),fill=GOLD)
    return im.convert('RGB')


def decode(path):
    r=subprocess.run([FF,'-v','error','-i',str(path),'-f','f32le','-ac','1','-ar','24000','pipe:1'],check=True,capture_output=True)
    return np.frombuffer(r.stdout,dtype='<f4').copy()


def encode_segment(item,tmp):
    idx,image,frames=item;dest=tmp/f'{idx:03d}.mp4'
    # One input image -> N frames, with 2% slow camera drift and short dissolves.
    duration=frames/FPS
    vf=f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},zoompan=z='1+0.02*on/{max(frames-1,1)}':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d={frames}:s={W}x{H}:fps={FPS},fade=t=in:st=0:d=0.22,fade=t=out:st={max(duration-.22,0):.4f}:d=0.22,format=yuv420p"
    cmd=[FF,'-v','error','-y','-i',str(image),'-vf',vf,'-frames:v',str(frames),'-an','-c:v','libx264','-preset','veryfast','-crf','25','-threads','2','-pix_fmt','yuv420p',str(dest)]
    subprocess.run(cmd,check=True)
    print(f'encoded {dest.name}: {duration:.2f}s',flush=True)
    return dest


def render_video(name,items,audio,tmp):
    tmp.mkdir(parents=True,exist_ok=True)
    work=[(i,image,frames) for i,(image,frames) in enumerate(items)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        paths=list(pool.map(lambda x:encode_segment(x,tmp),work))
    listing=tmp/'concat.txt';listing.write_text(''.join(f"file '{p}'\n" for p in paths))
    raw=tmp/'narration.f32';audio.astype('<f4').tofile(raw)
    out=ROOT/'video'/name
    subprocess.run([FF,'-v','error','-y','-f','concat','-safe','0','-i',str(listing),'-f','f32le','-ar','24000','-ac','1','-i',str(raw),'-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','96k','-movflags','+faststart','-shortest',str(out)],check=True)
    return out


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--temp',type=Path,default=Path('/tmp/fire-phoenix-render'));args=parser.parse_args()
    data=json.loads((ROOT/'metadata/chapters.json').read_text());chapters=data['chapters']
    for ch in chapters:plate(ch).save(ROOT/'cards'/f"chapter-{ch['number']:02d}.jpg",quality=91)
    poster('FIRE\nPHOENIX','A protected name. An earned awakening.\nA world that remembers.','00-approved-reference.png').save(ROOT/'POSTER.jpg',quality=94)
    poster('THE PUBLISHED\nCHRONICLE','52 chapters · narrated visual storyboard','00-approved-reference.png').save(ROOT/'cards/chronicle-intro.jpg',quality=92)
    poster('THE STALEMATE\nREMAINS','Chapter 52 ends here.\nThe herb remains rooted. Both beasts remain alive.','05-amiable-beasts.jpg').save(ROOT/'cards/chronicle-outro.jpg',quality=92)
    poster('FIRE\nPHOENIX','Reference-led concept art · English narration','00-approved-reference.png').save(ROOT/'cards/trailer-title.jpg',quality=92)
    poster('STRENGTH HAS\nA MEMORY','So does the world.','01-first-flight.jpg',small='AI-GENERATED MOTION PREVIEW · NOT OFFICIAL ANIMATION').save(ROOT/'cards/trailer-outro.jpg',quality=92)
    clips=[decode(next((ROOT/'audio').glob(f'{i:02d}-*.mp3'))) for i in range(10)]
    timeline=[];items=[];audios=[];cursor=0
    introframes=3*FPS;items.append((ROOT/'cards/chronicle-intro.jpg',introframes));audios.append(np.zeros(3*24000,dtype=np.float32));cursor=3.
    for group_i,start in enumerate(range(0,52,6),1):
        group=chapters[start:start+6];clip=clips[group_i]
        # A few samples of padding round the audio to exact video frame counts.
        totalframes=math.ceil(len(clip)/24000*FPS)+12
        weights=[len(f"Chapter {x['number']}. {x['title']}. {x['beat']}") for x in group]
        bounds=[round(totalframes*sum(weights[:i])/sum(weights)) for i in range(len(group)+1)]
        for i,ch in enumerate(group):
            frames=bounds[i+1]-bounds[i]
            timeline.append(dict(number=ch['number'],title=ch['title'],start=round(cursor,3),duration=round(frames/FPS,3),timing='estimated from narration text length; spoken chapter cues are authoritative'))
            items.append((ROOT/'cards'/f"chapter-{ch['number']:02d}.jpg",frames));cursor+=frames/FPS
        target=int(totalframes/FPS*24000);audios.append(np.pad(clip,(0,max(0,target-len(clip)))))
    items.append((ROOT/'cards/chronicle-outro.jpg',4*FPS));audios.append(np.zeros(4*24000,dtype=np.float32))
    chron=render_video('fire-phoenix-chapters-01-52.mp4',items,np.concatenate(audios),args.temp/'chronicle')
    # Trailer contains only reviewed images from this production, never rejected art.
    trailer_images=['06-extreme-north.jpg','00-approved-reference.png','07-first-bond.jpg','02-team336.jpg','03-protected-cocoon.jpg','01-first-flight.jpg','04-ranking-corridor.jpg','05-amiable-beasts.jpg']
    weights=[.10,.24,.09,.16,.08,.11,.06,.16]
    total=math.ceil(len(clips[0])/24000*FPS)
    bounds=[round(total*sum(weights[:i])) for i in range(len(weights)+1)]
    its=[(ROOT/'assets'/name,bounds[i+1]-bounds[i]) for i,name in enumerate(trailer_images)]
    its=[(ROOT/'cards/trailer-title.jpg',2*FPS)]+its+[(ROOT/'cards/trailer-outro.jpg',3*FPS)]
    trailer_audio=np.concatenate([np.zeros(2*24000,dtype=np.float32),clips[0],np.zeros(int((total/FPS-len(clips[0])/24000+3)*24000),dtype=np.float32)])
    trail=render_video('fire-phoenix-trailer.mp4',its,trailer_audio,args.temp/'trailer')
    output=dict(video_kind='Illustrated motion storyboard; no character animation or lip sync',fps=FPS,width=W,height=H,source_revision=data['source_revision'],chapter_timing='Approximate transitions; not word-aligned captions',chapters=timeline,outputs=[dict(file=str(p.relative_to(ROOT)),bytes=p.stat().st_size) for p in [chron,trail]])
    (ROOT/'metadata/render.json').write_text(json.dumps(output,indent=2)+'\n')
    print('RENDER COMPLETE',json.dumps(output['outputs']),flush=True)

if __name__=='__main__':main()
