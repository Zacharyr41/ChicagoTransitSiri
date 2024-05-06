import requests
import json
import constants
from urllib.parse import urlencode
from query_openai import extract_data, QueryType
from enum import Enum
from direction import Direction
import math
import sys
import os



class VehicleType(Enum):
    BUS = 1
    TRAIN = 2
    BOTH = 3
    NONE = 4


def query_geolocator(query: str, endpoint: str = "json?") -> json:
    query_parameters = {
        "address": query,
        "key": constants.GEOLOCATION_API_KEY,
    }
    encoded_params = urlencode(query_parameters)
    request_string = constants.GEOLOCATION_API_URI + endpoint + encoded_params
    resp = requests.get(request_string)

    return resp


def convert_query_to_latlong(query: str) -> tuple[float, float]:
    query_type = QueryType.ADDRESS
    # "Address: " is 9 characters long
    extracted_address = extract_data(
        query=query, query_type=query_type).content[9:]
    geolocator_query = extracted_address + " Chicago"
    geolocator_data = query_geolocator(query=geolocator_query)
    geolocator_data = geolocator_data.json()
    if len(geolocator_data['results']) > 0:
        answer = geolocator_data['results'][0]
        lat = answer['geometry']['location']['lat']
        long = answer['geometry']['location']['lng']
        return (lat, long)

    return (float('nan'), float('nan'))

def convert_query_to_vehicle(query: str) -> VehicleType:
    query_type = QueryType.VEHICLE
    vehicle_type_str = extract_data(query=query, query_type=query_type)
    vehicle_type_str = vehicle_type_str.content
    if vehicle_type_str == "BUS":
        return VehicleType.BUS
    elif vehicle_type_str == "TRAIN":
        return VehicleType.TRAIN
    elif vehicle_type_str == "BOTH":
        return VehicleType.BOTH
    
    return VehicleType.NONE

def convert_query_to_direction(query: str) -> str:
    query_type = QueryType.DIRECTION
    direction = extract_data(query=query, query_type=query_type)
    direction = direction.content[10:].strip()

    result = constants.STR_TO_DIRECTION_MAP[direction]

    return result


def convert_query_to_route_number(query: str) -> str:
    query_type = QueryType.ROUTE_NUMBER
    route_number = extract_data(query=query, query_type=query_type)
    route_number = route_number.content[7:]

    return route_number


if __name__ == "__main__":
    new_qry = "When is the 172 going to arrive?"
    #res = convert_query_to_latlong(new_qry)
    res = convert_query_to_route_number(new_qry)
    print("res: ", res)
    