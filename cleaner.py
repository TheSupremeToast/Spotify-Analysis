import numpy as np
import pandas as pd
import time
import datetime

##################
### cleaner.py ###
##################

# clean up spotify input data and sort into pandas dataframes

##################

# Convert json files to pandas dataframe
# directory - the folder directory containing the json files
def read_history(directory):
    his_list = []
    i = 0
    for file in os.scandir(directory):
        if (file.path.endswith('.json') and file.is_file() and 'StreamingHistory' in file.path):
            i = i + 1
            temp = pd.read_json(file.path)
            his_list.append(temp)
    his = pd.concat(his_list)
    print('Files Included:', i, '\n')
    print('Unique Values:')
    print(his.apply(lambda x: x.nunique()))
    return his

##################

#
# Create a new dataframe for songs that were not skipped
# (> 30s playtime)
#
# his: history dataframe from read_history
#
def sort_unskipped(his):
    unskipped = his[his['msPlayed'] > 30000]

    # This line causes minor error, fix at some point - currently necessary for timeframe functions to work
    unskipped['endTime'] = pd.to_datetime(unskipped['endTime'])
    
    return(unskipped)

#
# Create a new dataframe for songs that were skipped
# (< 30s playtime)
#
# his: history dataframe from read_history
#
def sort_skipped(his):
    # sort songs into skipped and unskipped categories
    skipped = his[his['msPlayed'] < 30000]
    return(skipped)

##################

# get list of most played songs (sorted descending) 
# his: dataframe to pull from
def get_tracks(his):
    tracks = his['trackName'].value_counts()
    return(tracks)

# get list of most played artists (sorted descending) 
# his: dataframe to pull from
def get_artists(his):
    artists = unskipped['artistName'].value_counts() 
    return(artists)

# for relative frequency add 'normalize = True' within value_counts()

# outdated - use get functions with skipped df
# skipped_tracks = skipped['trackName'].value_counts()
# skipped_artists = skipped['artistName'].value_counts()

##################

# ENDFILE
