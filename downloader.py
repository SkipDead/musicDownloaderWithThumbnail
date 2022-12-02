import re
from pytube import YouTube
import os
from pathlib import Path


def youtube2mp3 (url,outdir):
    # url input from user
    yt = YouTube(url)

    video = yt.streams.get_audio_only()
    ##@ Downloadthe file
    out_file = video.download(output_path=outdir)
    mp3_filename = re.sub(' +', ' ', out_file)
    mp3_filename = mp3_filename[:-4] + ".mp3"
    cmd = f"ffmpeg -i \"{out_file}\" -vn \"{mp3_filename}\""
    os.system(cmd)
    print(f"done converting to mp3 {mp3_filename}")
    os.remove(out_file)
    return mp3_filename