#!/usr/bin/env python3
"""Create explicitly estimated English WebVTT sidecars, not forced alignment."""
from pathlib import Path
import json,re,subprocess,textwrap
import imageio_ffmpeg
ROOT=Path(__file__).resolve().parents[1]

def stamp(t):
    ms=round(t*1000);h,ms=divmod(ms,3600000);m,ms=divmod(ms,60000);s,ms=divmod(ms,1000)
    return f'{h:02d}:{m:02d}:{s:02d}.{ms:03d}'

def write(path,cues):
    lines=['WEBVTT','','NOTE','Estimated timing, not word-aligned. Spoken chapter cues are authoritative.','']
    for i,(start,end,text) in enumerate(cues,1):
        lines += [str(i),f'{stamp(start)} --> {stamp(end)}',textwrap.fill(text,width=68),'']
    path.write_text('\n'.join(lines)+'\n')

def main():
    chapters=json.loads((ROOT/'metadata/chapters.json').read_text())['chapters']
    timings=json.loads((ROOT/'metadata/render.json').read_text())['chapters']
    cues=[(x['start'],x['start']+x['duration'],f"Chapter {ch['number']}. {ch['title']}. {ch['beat']}") for x,ch in zip(timings,chapters)]
    write(ROOT/'video/fire-phoenix-chapters-01-52.en.vtt',cues)
    r=subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(),'-v','error','-i',str(ROOT/'audio/00-trailer.mp3'),'-f','f32le','-ar','24000','-ac','1','pipe:1'],check=True,capture_output=True)
    duration=len(r.stdout)/4/24000
    sentences=re.split(r'(?<=[.!?])\s+',(ROOT/'audio/00-script.txt').read_text().strip())
    total=sum(len(x) for x in sentences);t=2.;cues=[]
    for s in sentences:
        end=t+duration*len(s)/total;cues.append((t,end,s));t=end
    write(ROOT/'video/fire-phoenix-trailer.en.vtt',cues)
    print('Estimated English captions written for both videos.')

if __name__=='__main__':main()
