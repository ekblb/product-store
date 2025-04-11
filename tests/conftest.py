import pytest
import requests

from configuration import SERVICE_URL


@pytest.fixture
def get_items():
    response = requests.get(url=SERVICE_URL)
    return response


def function(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return (a + b)
    else:
        return None


@pytest.fixture
def function_fixture():
    return function
