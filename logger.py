#################
### logger.py ###
#################

# Perpetually log user's currently playing song
# keep track of starting and ending times
# maybe also get song length?

#################

import os, time, json, spotipy
from json_helper import write_json
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

load_dotenv()
client = os.getenv('SPOTIFY_CLIENT_ID')
secret = os.getenv('SPOTIFY_CLIENT_SECRET')
uri = os.getenv('SPOTIFY_REDIRECT_URI')

client_auth = SpotifyClientCredentials()
client = spotipy.Spotify(auth_manager = client_auth)


#################

# scopes
scope = 'user-read-currently-playing user-read-playback-state user-library-read'
sp = spotipy.Spotify(auth_manager = SpotifyOAuth(scope = scope))

#
# make spotify api call to get currently playing song
#
def log_history():
    print('Logging started...')
    while(True):
        try:
            playing = sp.current_user_playing_track()
            # dump = json.dumps(playing, indent = 2)
            # write_json(dump, 'output/raw_history.json')
            write_json(playing, 'output/raw_history.json')
            print(f'Song logged: {time.asctime(time.gmtime())}')
            time.sleep(5)
        except KeyboardInterrupt:
            print("\nExit signal received.")
            break

