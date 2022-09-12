###################
### json_helper ###
###################

# helper functions for dealing with json files

###################

import json, os

###################

#
# generate json with defined schema
# NOTE: will overwrite old json file
#
def create_json(filename):
    with open(filename, 'w') as file:
        file.write('{\n  "history": [\n\n  ]\n\n}')

def create_json_alt(filename):
    with open(filename, 'w') as file:
        file.write('[\n\n  ]')
#
# add to existing json file
#
def write_json(new_data, filename):
    with open(filename, 'r+') as file:
        #load existing data into dictionary
        file_data = json.load(file)
        # join new_data with file_data inside users
        file_data['history'].append(new_data)
        # set current position in file
        file.seek(0)
        # convert back to json
        json.dump(file_data, file, indent = 2)

def write_json_alt(new_data, filename):
    with open(filename, 'r+') as file:
        #load existing data into dictionary
        file_data = json.load(file)
        # join new_data with file_data inside users
        file_data.append(new_data)
        # set current position in file
        file.seek(0)
        # convert back to json
        json.dump(file_data, file, indent = 2)

