from direction import Direction

GEOLOCATION_API_URI = "https://maps.googleapis.com/maps/api/geocode/"
GEOLOCATION_API_KEY = ""# Insert Key

QUERY_TO_ADDRESS_FILENAME = "query_to_address_instructions.txt"
QUERY_TO_VEHICLE_FILENAME = "query_to_identify_bus_or_train.txt"
QUERY_TO_ROUTE_FILENAME = "bus_number.txt"
QUERY_TO_DIRECTION_FILENAME = "direction.txt"

GPT_MODEL = "gpt-3.5-turbo"

STOP_DISTANCE_THRESHHOLD = 100

DIRECTION_TO_STR_MAP = {
    Direction.NORTHBOUND: "Northbound",
    Direction.SOUTHBOUND: "Southbound",
    Direction.EASTBOUND: "Eastbound",
    Direction.WESTBOUND: "Westbound",
    Direction.NONE: "NONE"
}

STR_TO_DIRECTION_MAP = {
    "Northbound": Direction.NORTHBOUND,
    "Southbound": Direction.SOUTHBOUND,
    "Eastbound": Direction.EASTBOUND,
    "Westbound": Direction.WESTBOUND,
    "NONE": Direction.NONE
}
