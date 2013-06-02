from muni_data_client import _collect_states_data
from muni_data_client import assign_guids
from muni_data_client import write_state_data

def main():
    state_list = ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'de', 'fl', 'ga', 'hi', 'id', 'il', 'in', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi', 'mn', 'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd', 'oh', 'ok', 'or', 'pa', 'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy', 'as', 'dc', 'fm', 'gu', 'mh', 'mp', 'pw', 'pr', 'vi']
    states_data = _collect_states_data(state_list)
    for state_data in states_data:
        data_identified = assign_guids(state_data[1])
        write_state_data(state_data[0], list(data_identified), "out")


if __name__ == '__main__':
    main()