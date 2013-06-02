from itertools import imap
import uuid
import os
import json

def _assign_guid(city_or_county_data):
    data = city_or_county_data.copy()
    data['guid'] = uuid.uuid4().hex
    return data

def assign_guids(city_county_data_of_state):
    return imap(_assign_guid, city_county_data_of_state)

def write_state_data(state, data, project_dir=""):
    try:
        if project_dir:
            os.makedirs(project_dir)
    except OSError:
        pass
    state_file = open(os.path.join(project_dir, "{0}.json".format(state)),'w')
    json.dump(data, state_file)
