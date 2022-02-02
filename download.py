from turtle import down
import youtube_dl
import urllib.request
import re

f = open('output.txt', 'r')
song_names = f.read().splitlines()
f.close()

def download(i):
    #get the link part
    print(song_names[i])
    
    html =  urllib.request.urlopen(f"https://www.youtube.com/results?search_query={song_names[i].replace(' ','%20').replace('-', '%2d')}")
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    print(f"https://www.youtube.com/watch?v={video_ids[0]}")

    #downloading part
    filename = f'{song_names[i]}.mp3'
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([f"https://www.youtube.com/watch?v={video_ids[0]}"])

    print('download complete.. {}'.format(filename))

for i in range(len(song_names)-1):
    download(i)