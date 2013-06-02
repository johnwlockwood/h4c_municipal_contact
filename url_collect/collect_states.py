from muni_data_client import _collect_states_data
from muni_data_client import assign_and_write_state_data

from functools import partial
from itertools import starmap

assign_and_write_state_data_out = partial(assign_and_write_state_data,
                                          project_dir="out")

def main():
    state_list = ['al', 'ak', 'az', 'ar', 'ca', 'co',
                  'ct', 'de', 'fl', 'ga', 'hi', 'id',
                  'il', 'in', 'ia', 'ks', 'ky', 'la',
                  'me', 'md', 'ma', 'mi', 'mn', 'ms',
                  'mo', 'mt', 'ne', 'nv', 'nh', 'nj',
                  'nm', 'ny', 'nc', 'nd', 'oh', 'ok',
                  'or', 'pa', 'ri', 'sc', 'sd', 'tn',
                  'tx', 'ut', 'vt', 'va', 'wa', 'wv',
                  'wi', 'wy', 'as', 'dc', 'fm', 'gu',
                  'mh', 'mp', 'pw', 'pr', 'vi']
    list(starmap(assign_and_write_state_data_out,
                 _collect_states_data(state_list)))


if __name__ == '__main__':
    main()
