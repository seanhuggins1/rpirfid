import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import rfidReader
import time
from beepy import beep


rfidTrackDict = {
    "486758229519": "spotify:track:6U0FIYXCQ3TGrk4tFpLrEA",
    "962702287203": "spotify:track:5aZhRbJSzAuedzUF3Rv78q"
}

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')

auth_manager=SpotifyOAuth(
    scope="user-modify-playback-state,user-read-playback-state",
)

client = spotipy.Spotify(auth_manager=auth_manager)

while True:
    print("Waiting for you to scan an RFID sticker/card")
    id = rfidReader.readId()
    beep(sound=1)
    
    trackId = rfidTrackDict.get(str(id), None)
    if (trackId != None):
        uris = [rfidTrackDict[str(id)]]
        client.start_playback(uris=uris)
        print("Waiting before scanning again...")
        time.sleep(3)
    else:
        print("This RFID is not registered:", id)