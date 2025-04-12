import pytest
import requests

from configuration import SERVICE_URL
from src.generators.message import Message


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


@pytest.fixture
def get_message_generator():
    return Message()
