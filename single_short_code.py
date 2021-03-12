import youtube_dl
import os.path
from os import path


from instaloader import Instaloader, Post

shortcode = "Bm1rDT1hTbD"

file_path = 'BNknWGJD8Lx/2016-12-03_22-40-50_UTC.mp4'

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


if path.isfile(file_path):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(file_path)



