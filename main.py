import spotipy
from vars import Client_ID,Client_Secret
from spotipy.oauth2 import SpotifyClientCredentials

ccm = SpotifyClientCredentials(client_id=Client_ID, client_secret=Client_Secret)
sp = spotipy.Spotify(client_credentials_manager=ccm)

def songList():
    f = open("output.txt", 'w')

    plink = input("Enter spotify playlist url: ")
    pURI = plink.split("/")[-1].split("?")[0]
    #trackURIs = [x["track"]["uri"] for x in sp.playlist_tracks(pURI)["items"]]
    
    for track in sp.playlist_tracks(pURI)["items"]:
        track_name = track["track"]["name"]
        f.write(track_name + '\n')

    print('epic')

songList()
