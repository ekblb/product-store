import requests

from jsonschema import validate

from configuration import SERVICE_URL

from src.base_classes.response import Response
from src.schemas.item import ITEMS_SCHEMA


def test_getting_items():
    response = requests.get(url=SERVICE_URL)
    recieved_response = Response(response)

    recieved_response.assert_status_code(200).validate(ITEMS_SCHEMA)