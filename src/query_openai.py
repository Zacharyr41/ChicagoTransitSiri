from openai import OpenAI
from enum import Enum
import os
import constants


class QueryType(Enum):
    ADDRESS = 1
    VEHICLE = 2
    ROUTE_NUMBER = 3
    DIRECTION = 4


def extract_data(query: str, query_type: QueryType) -> str:
    client = OpenAI()
    path_to_prompt_file = "./data/"

    if query_type == QueryType.ADDRESS:
        path_to_prompt_file += constants.QUERY_TO_ADDRESS_FILENAME
    elif query_type == QueryType.VEHICLE:
        path_to_prompt_file += constants.QUERY_TO_VEHICLE_FILENAME
    elif query_type == QueryType.ROUTE_NUMBER:
        path_to_prompt_file += constants.QUERY_TO_ROUTE_FILENAME
    else:
        path_to_prompt_file += constants.QUERY_TO_DIRECTION_FILENAME

    message_list = []
    with open(path_to_prompt_file, 'r') as prompt_file:
        system_prompt = prompt_file.read()
        message_list.append({"role": "system", "content": system_prompt})
    message_list.append({"role": "user", "content": query})

    completion = client.chat.completions.create(
        model=constants.GPT_MODEL,
        messages=message_list
    )

    return completion.choices[0].message


if __name__ == "__main__":
    query_type = QueryType.DIRECTION
    query = "When is the 172 that goes south bus leaving 60th and university?"

    result = extract_data(query=query, query_type=query_type)
    print("Res: ", result.content)
