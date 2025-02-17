import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

# Load API keys
load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Authenticate
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))

def get_playlist(emotion):
    """Find a playlist matching the detected emotion"""
    query = f"{emotion} mood playlist"
    results = sp.search(q=query, type='playlist', limit=1)
    
    if results['playlists']['items']:
        return results['playlists']['items'][0]['external_urls']['spotify']
    return "No playlist found."

if __name__ == "__main__":
    print(get_playlist("happy"))  # Should return a Spotify playlist link
