
import json
import os
import sys
import constants
from util import pythagorean_distance, convert_processed_prediction_to_sentenced
from direction import Direction

sys.path.append(
    '/Users/zacharyrothstein/Documents/transit-hackathon-zach/cta_analysis')
import train
import bus


def get_all_nearby_bus_stops(loc: tuple[float, float]) -> list[dict]:
    nearby_stops = []

    this_lat = loc[0]
    this_lng = loc[1]
    with open('./data/all_stops.json', 'r') as file:
        stop_data = json.load(file)

    for route_number in stop_data:
        for direction in stop_data[route_number]:
            cur_stops = stop_data[route_number][direction]
            for stop in cur_stops:
                cur_dist = pythagorean_distance(
                    this_lat, this_lng, stop['lat'], stop['lon'])
                if cur_dist <= constants.STOP_DISTANCE_THRESHHOLD:
                    nearby_stops.append(stop['stpid'])

    return nearby_stops


def process_predictions_from_stops(stop_id_list: list[str]) -> list[dict]:
    result = []
    predictions_from_stops = bus.get_predictions_from_stops(stop_id_list)
    for prediction in predictions_from_stops:
        time = prediction["prdctdn"]
        if time == 'DUE':
            time = '0'
        if time == 'DLY':
            time = '-999'
        prediction_dict = {
            "stop_id": prediction['stpid'],
            "stop_name": prediction['stpnm'],
            "time_until_arrival": int(time),
            "route_number": str(prediction['rt']),
            "direction": prediction['rtdir'],
            "destination": prediction['des']
        }
        result.append(prediction_dict)

    return result


def filter_predictions(processed_predictions: list[dict], route_num: str, direction: Direction) -> list[dict]:
    result = []
    route_num_as_int = int(route_num)

    if route_num_as_int <= 0 and direction == Direction.NONE:  # Do not filter
        return processed_predictions
    elif route_num_as_int <= 0 and direction != Direction.NONE:  # Filter only based on Direction
        for pred in processed_predictions:
            if pred['direction'] == constants.DIRECTION_TO_STR_MAP[direction]:
                result.append(pred)
    elif route_num_as_int > 0 and direction == Direction.NONE:  # Filter only based on route number
        for pred in processed_predictions:
            if pred['route_number'] == route_num:
                result.append(pred)
    else:  # Filter based on both route number and Direction
        for pred in processed_predictions:
            if pred['direction'] == constants.DIRECTION_TO_STR_MAP[direction] and pred['route_number'] == route_num:
                result.append(pred)
    return result


def verbalize_predictions(processed_predictions: list[dict]) -> list[str]:
    result = []
    for prediction in processed_predictions:
        verbalized = convert_processed_prediction_to_sentenced(prediction)
        result.append(verbalized)
    return result


def verbalized_from_latlong(loc: tuple[float, float], route_num: str = '-1', direction: Direction = Direction.NONE) -> list[str]:
    nearby_stops = get_all_nearby_bus_stops(loc=loc)
    processed_predictions = process_predictions_from_stops(stop_id_list=nearby_stops)
    filtered_predictions = filter_predictions(processed_predictions=processed_predictions, route_num=route_num, direction=direction)
    verbalized_predictions = verbalize_predictions(filtered_predictions)
    return verbalized_predictions


if __name__ == "__main__":
    ex_tup = (41.7995763, -87.5873804)
    res = verbalized_from_latlong(loc=ex_tup, route_num='28', direction=Direction.SOUTHBOUND)
    print("res: ", res)
