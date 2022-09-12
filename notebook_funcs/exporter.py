import os
from pathlib import Path
import pandas as pd

from cleaner import *
from helper import *

directory = Path('input/07-02-22') # change this to '/input/your-directory-name'
his = read_history(directory)

skipped = sort_skipped(his)
unskipped = sort_unskipped(his)

tracks = get_tracks(unskipped)
artists = get_artists(unskipped)

plotArtist("The Strokes", 20)
