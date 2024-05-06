from sanic import Sanic
from sanic.response import json
from sanic.response import text
from direction import Direction
import query_handler
import cta_data

import os


app = Sanic(__name__)


@app.route("/chat", methods=['POST'])
async def chat(request):
    print("Request Received")
    request_json = request.json
    query = request_json['query']
    print("Query: ", query)
    lat_long_tup = query_handler.convert_query_to_latlong(query=query)
    route_num = query_handler.convert_query_to_route_number(query=query)
    direction = query_handler.convert_query_to_direction(query=query)
    verbalized_predictions = cta_data.verbalized_from_latlong(loc=lat_long_tup, route_num=route_num, direction=direction)

    res = ""
    for pred in verbalized_predictions:
        res += pred + "\n"
    print("RES: ", res)

    return text(res)


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)), auto_reload=True)