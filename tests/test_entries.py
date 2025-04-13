import pytest

from src.base_classes.response import Response
from src.pydantic.item import Item
from src.generators.text_language import TextLocalization


def test_getting_items(get_items):
    """
    Getting list of items
    """
    Response(get_items).assert_status_code(200).validate(Item)


@pytest.mark.skip('test skipping')
def test_for_skip():
    """
    Try to skip the test
    """
    print('need to skip')


@pytest.mark.development
@pytest.mark.parametrize(
    'first_value, second_value, result', [
        (1, 2, 3), (-1, 3, 2), ('a', 3, None)
        ])
def test_function_in_fixture(first_value, second_value, result,
                             function_fixture):
    """
    Try to use various parameters within one test
    """
    assert function_fixture(first_value, second_value) == result


@pytest.mark.parametrize(
        'name_in_message', ['Katya', '', None]
        )
def test_generator_messages(name_in_message, get_message_generator):
    """
    Try to use generator in test
    """
    name_different_text = get_message_generator.build()
    name_different_text['name'] = name_in_message
    print(name_different_text)


@pytest.mark.parametrize(
        'delete_key', ['email', 'name', 'message']
        )
def test_messages_without_key(delete_key, get_message_generator):
    """
    Delete keys in generator
    """
    message_without_key = get_message_generator.build()
    del message_without_key[delete_key]
    print(message_without_key)


@pytest.mark.parametrize(
        "language_message, language_generator", [
            ('en', 'en_US'), ('ru', 'ru_RU')
            ])
def test_generation_for_deep_objects(language_message, language_generator,
                                     get_message_generator):
    """
    Try to update values only in deep objects
    """
    message_update_deep_params = get_message_generator.update_deep_params(
        ['message', language_message],
        TextLocalization(language_generator).build()).build()
    print(message_update_deep_params)
