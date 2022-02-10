import os
import time
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials
# Allow user to grant permissions only once
from spotipy.oauth2 import SpotifyOAuth

from dotenv import load_dotenv

# get token as environment variable
load_dotenv()
client = os.getenv('SPOTIFY_CLIENT_ID')
secret = os.getenv('SPOTIFY_CLIENT_SECRET')
uri = os.getenv('SPOTIFY_REDIRECT_URI')

# prompt login?
# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# Set scope to target user library
# scope = 'user-library-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = client, 
    client_secret = secret, redirect_uri = uri))

# get user's top tracks
# - limit: number of entries to return
# - offset: first entity to return
# - time_range = short_term, medium_term, long_term
# results = sp.current_user_top_tracks()

# get user's top artists
# - limit: number of entries to return
# - offset: first entity to return
# - time_range = short_term, medium_term, long_term
sp.current_user_top_artists(25, time_range = 'short_term')

# get user's playlists
# results = sp.current_user_playlists()
