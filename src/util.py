import math

# Used ChatGPT for this
def pythagorean_distance(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers (approx)
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Change in coordinates in radians
    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    # Approximation of distance in latitude and longitude directions
    delta_x = delta_lon * R * math.cos((lat1_rad + lat2_rad) / 2)
    delta_y = delta_lat * R

    # Convert deltas from kilometers to meters
    delta_x = delta_x * 1000
    delta_y = delta_y * 1000

    # Pythagorean theorem to find straight line distance in meters
    distance = math.sqrt(delta_x**2 + delta_y**2)

    return distance


def convert_processed_prediction_to_sentenced(prediction : dict) -> str:
    direction = prediction['direction']
    route_number = prediction['route_number']
    destination = prediction['destination']
    stop_name = prediction['stop_name']
    stop_id = prediction['stop_id']
    time = prediction['time_until_arrival']
    return f"The {direction} bus {route_number} to {destination} will arrive at {stop_name} (Stop ID: {stop_id}) in {time} minutes."