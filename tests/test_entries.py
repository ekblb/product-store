import requests

from configuration import SERVICE_URL

from src.base_classes.response import Response
from src.pydantic.item import Item


def test_getting_items():
    response = requests.get(url=SERVICE_URL)
    recieved_response = Response(response)

    recieved_response.assert_status_code(200).validate(Item)