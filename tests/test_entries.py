from src.base_classes.response import Response
from src.pydantic.item import Item


def test_getting_items(get_items):
    Response(get_items).assert_status_code(200).validate(Item)
