import pytest

from src.base_classes.response import Response
from src.pydantic.item import Item


def test_getting_items(get_items):
    Response(get_items).assert_status_code(200).validate(Item)


@pytest.mark.skip('test skipping')
def test_for_skip():
    print('need to skip')


@pytest.mark.development
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3), (-1, 3, 2), ('a', 3, None)
        ])
def test_funtion_in_fixture(first_value, second_value, result,
                            function_fixture):
    assert function_fixture(first_value, second_value) == result
