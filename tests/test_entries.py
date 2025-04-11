import pytest

from src.base_classes.response import Response
from src.pydantic.item import Item


def test_getting_items(get_items):
    Response(get_items).assert_status_code(200).validate(Item)


@pytest.mark.skip('test skipping')
def test_for_skip():
    print('need to skip')
