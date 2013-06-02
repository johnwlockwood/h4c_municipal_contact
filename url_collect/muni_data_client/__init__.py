from itertools import imap
from itertools import ifilter
import uuid
import os
import json
import requests


def _collect_url_json(url):
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()
            return data
        except ValueError:
            pass

def _collect_state_data(state):
    url = "http://api.sba.gov/geodata/" \
          "city_county_data_for_state_of/{0}.json".format(state)
    data = _collect_url_json(url)
    if data:
        return (state, data)


def _collect_states_data(states):
    return ifilter(lambda x: x is not None,
                   imap(_collect_state_data, states))


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
