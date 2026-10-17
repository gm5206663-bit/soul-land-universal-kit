#!/usr/bin/env python3
"""Optional UI QA: pip install playwright && playwright install chromium.

Start a local static HTTP server before using the default URL. Screenshots are
scratch QA files, not new illustrations. Public URL checks may use --output to
store their receipt outside the immutable release pack.
"""
from pathlib import Path
import argparse,json
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--url',default='http://127.0.0.1:8080/');ap.add_argument('--output',type=Path,default=ROOT/'metadata/browser-checks.json');ap.add_argument('--screenshots',type=Path,default=Path('/tmp/fire-phoenix-render/review'));a=ap.parse_args()
    a.screenshots.mkdir(parents=True,exist_ok=True)
    with sync_playwright() as p:
        b=p.chromium.launch(headless=True,args=['--no-sandbox'])
        page=b.new_page(viewport={'width':1440,'height':1040},device_scale_factor=1)
        errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
        response=page.goto(a.url,wait_until='networkidle')
        assert response.status==200
        assert page.locator('.chapter').count()==52
        assert page.locator('.art').count()==8
        page.select_option('#filter','art');assert page.locator('.chapter:visible').count()==10
        page.select_option('#filter','plan');assert page.locator('.chapter:visible').count()==42
        page.select_option('#filter','all');page.fill('#search','Amiable Beasts');assert page.locator('.chapter:visible').count()==1
        page.locator('.chapter:visible .image-open').click();assert page.locator('dialog').is_visible();page.click('#close');assert not page.locator('dialog').is_visible()
        page.fill('#search','');page.evaluate('window.scrollTo(0,0)');page.screenshot(path=str(a.screenshots/'gallery-desktop.png'))
        # Exercise actual video playback, not just an HTTP or metadata request.
        page.evaluate("async()=>{const v=document.querySelector('video');v.muted=true;await v.play()}")
        page.wait_for_function("document.querySelector('video').currentTime>0.6",timeout=20000)
        playback=page.evaluate("()=>{const v=document.querySelector('video');v.pause();return {duration:v.duration,currentTime:v.currentTime,width:v.videoWidth,height:v.videoHeight,error:v.error&&v.error.code}}")
        assert playback['width']==1280 and playback['height']==720 and not playback['error']
        page.set_viewport_size({'width':390,'height':844});page.evaluate('window.scrollTo(0,0)');page.screenshot(path=str(a.screenshots/'gallery-mobile.png'))
        overflow=page.evaluate('document.documentElement.scrollWidth > window.innerWidth')
        assert not overflow,'Mobile horizontal overflow'
        assert not errors,errors
        report=dict(passed=True,url=a.url,chapter_cards=52,scene_illustrations=8,filters={'illustrated_chapter_entries':10,'scene_art_planned':42},search=True,lightbox=True,mobile_no_horizontal_overflow=True,video_playback=playback,javascript_errors=errors)
        a.output.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));b.close()

if __name__=='__main__':main()
