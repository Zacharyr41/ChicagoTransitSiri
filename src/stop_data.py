import sys
import json
sys.path.append('/Users/zacharyrothstein/Documents/transit-hackathon-zach/cta_analysis')

import bus

# Run to get all bus stops and save locally, Refresh daily
def save_bus_stops_to_json():
    all_stops_dict = bus.get_all_stops()
    all_stops_filename = './data/all_stops.json'
    with open(all_stops_filename, 'w') as file:
        json.dump(all_stops_dict, file, indent=4)


if __name__ == "__main__":
    save_bus_stops_to_json()