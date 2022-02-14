import os
import time
import spotipy

##################
### pi_spot.py ###
##################

##################

# Server to server requests - doesn't require user auth

# Set up client credential flow for non-user information requests
from spotipy.oauth2 import SpotifyClientCredentials

from dotenv import load_dotenv

# get token as environment variable
# application authentication variables
load_dotenv()
client = os.getenv('SPOTIFY_CLIENT_ID')
secret = os.getenv('SPOTIFY_CLIENT_SECRET')
uri = os.getenv('SPOTIFY_REDIRECT_URI')

client_auth = SpotifyClientCredentials()
client = spotipy.Spotify(auth_manager = client_auth)

##################

# user to server requests - requires oauth

# Allow user to grant permissions only once
from spotipy.oauth2 import SpotifyOAuth

# Authenticate to access individual user data
scope = 'user-library-read'
# user = spotipy.Spotify(auth_manager = SpotifyOAuth(scope = scope))

##################

# get user's top tracks
# - limit: number of entries to return
# - offset: first entity to return
# - time_range = short_term, medium_term, long_term
scope = 'user-top-read'
user = spotipy.Spotify(auth_manager = SpotifyOAuth(scope = scope))
results = user.current_user_top_tracks()

# get user's top artists
# - limit: number of entries to return
# - offset: first entity to return
# - time_range = short_term, medium_term, long_term
# user.current_user_top_artists(25, time_range = 'short_term')

# get user's playlists
# results = user.current_user_playlists()

print(results)



##################

# ENDFILE
