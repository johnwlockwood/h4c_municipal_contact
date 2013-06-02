import json
import os

from muni_data_client import assign_guids
from muni_data_client import write_state_data

def main():
    test_state_file = open(os.path.join('test_data', 'ar.json'),'r')
    data = json.load(test_state_file)
    data_identified = list(assign_guids(data))
    write_state_data('ar', data_identified, "out")


if __name__ == '__main__':
    main()
