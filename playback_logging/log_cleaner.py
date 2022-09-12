######################
### log_cleaner.py ###
######################

import os, time
import orjson
from playback_logging import json_helper 
from src.utils import get_project_root

######################

# TODO: optimize, likely rewrite in C/rust/go or msgspec library for python
# - last option requires changes to json_helper and logger
# - handle rapidly growing raw file
# - maybe base it on the date?

# -> figure out if I want to deal with pauses (api gives new timestamp)
#   - compare timestamps, see if they are close? (and/or compare song names)


'''
convert raw_history.json into more usable file
'''
def clean_logs(path, make_new = False):
    rootdir = get_project_root()
    # check to generate new clean json output file
    if make_new:    
        json_helper.create_json_alt(f'{rootdir}/output/history.json')

    # json
    # with open('output/raw_history.json', 'r') as f:
    #     data = json.load(f)

    # orjson
    with open(f'{rootdir}/output/raw_history.json', 'rb') as f:
        data = orjson.loads(f.read())

    # initual conditions
    count = 0
    skipped = 0
    completed = False
    prev_timestamp = data['history'][0]['timestamp']

    for entry in data['history']:
        if entry == None: 
            count +=1
            continue

        # timestamp = data['history'][count]['timestamp']
        timestamp = entry['timestamp']
        if prev_timestamp != timestamp:
            # define json dictionary output format
            count -= 1
            progress = data['history'][count]['progress_ms']
            duration = data['history'][count]['item']['duration_ms']

            # spotify metric for skips
            if 30000 <= progress <= duration:
                skipped = False
            else:
                skipped = True

            # broader skip definition
            if duration - 8000 <= progress <= duration:
                completed = True
            else:
                completed = False

            new_entry = {
                "timestamp": timestamp,
                "track_id": data['history'][count]['item']['id'],
                "track_name": data['history'][count]['item']['name'],
                "artist_name": data['history'][count]['item']['artists'][0]['name'],
                "album_name": data['history'][count]['item']['album']['name'],
                "progress_ms": progress,
                "duration_ms": duration,
                "skipped": skipped,
                "completed": completed,
                "popularity": data['history'][count]['item']['popularity'],
                "explicit": data['history'][count]['item']['explicit'],
                "track_uri": data['history'][count]['item']['uri'],
                "artist_uri": data['history'][count]['item']['artists'][0]['uri'],
                "album_uri": data['history'][count]['item']['album']['uri'],
                "context_uri": data['history'][count]['context']['uri'],
                "album_image": data['history'][count]['item']['album']['images'][0]['url'],
            }

            count +=1
            json_helper.write_json_alt(new_entry, f'{rootdir}/output/history.json')

        prev_timestamp = timestamp
        count+=1

        # end of loop
    return 0

