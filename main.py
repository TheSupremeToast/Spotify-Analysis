import pandas as pd
import matplotlib.pyplot as plt
import sys, os, os.path
from pathlib import Path
import time, datetime

from notebook_funcs.cleaner import *
from notebook_funcs.helper import *
from notebook_funcs.live import *

if len(sys.argv) < 2:
    print('Error: not enough inputs')
    exit(1)

directory = Path(f'{sys.argv[1]}')
his = read_history(directory)

skipped = sort_skipped(his)
unskipped = sort_unskipped(his)

tracks = get_tracks(unskipped)
artists = get_artists(unskipped)

print('\n')

plotTopTracks(tracks, 50, True)
plotTopArtists(artists, 50, True)

# TODO: parameterize dates
lower = '2022-01-01'
upper = '2022-10-30'

topSongs = topSongsTimeframeBounded(lower, upper, 10, True, True)
topArtists = topArtistsTimeframeBounded(lower, upper, 10, True, True)
# FIX: these error out
# topSkippedSongs = mostSkippedTimeframeBounded(lower, upper, 10, True, True)
# topSkippedArtists = mostSkippedArtistsTimeframeBounded(lower, upper, 10, True, True)


