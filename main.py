import spotipy
from vars import Client_ID,Client_Secret
from spotipy.oauth2 import SpotifyClientCredentials
import youtube_dl
import urllib.request
import re

ccm = SpotifyClientCredentials(client_id=Client_ID, client_secret=Client_Secret)
sp = spotipy.Spotify(client_credentials_manager=ccm)

def songList(plink):
    f = open("output.txt", 'w')

    pURI = plink.split("/")[-1].split("?")[0]
    #trackURIs = [x["track"]["uri"] for x in sp.playlist_tracks(pURI)["items"]]
    
    for track in sp.playlist_tracks(pURI)["items"]:
        track_name = track["track"]["name"]
        artist_name = track["track"]["artists"][0]["name"]
        f.write(track_name + " - " + artist_name + '\n')

    print('epic')

def download():
    f = open('output.txt', 'r')
    song_names = f.read().splitlines()
    f.close()

    for i in range(len(song_names)-1):
        print(song_names[i])
        video_ids = re.findall(r"watch\?v=(\S{11})", urllib.request.urlopen(f"https://www.youtube.com/results?search_query={song_names[i].replace(' ','%20').replace('-', '%2d')}").read().decode())
        print(f"https://www.youtube.com/watch?v={video_ids[0]}")

        filename = f'{song_names[i]}.mp3'
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':filename,
        }
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([f"https://www.youtube.com/watch?v={video_ids[0]}"])
        print('download complete.. {}'.format(filename))

plink = input("Enter spotify playlist url: ")
try:
    songList(plink)
except:
    print('There is an error!')

confirm_dwnld = input("Do you want to download all of songs?(Y/N): ").lower()
if confirm_dwnld == 'y':
    download()
else:
    print('Ok!')
