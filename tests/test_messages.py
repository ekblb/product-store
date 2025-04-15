import pytest

from src.generators.text_language import TextLocalization
from src.enums.message_enums import Status, MessageFields


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
        'delete_key', [*MessageFields.list()]
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


@pytest.mark.parametrize("status_params", [*Status.list()])
def test_pydantic_in_parametrize(status_params, get_message_generator):
    print(get_message_generator.set_status(status_params).build())
