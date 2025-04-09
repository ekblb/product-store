# from jsonschema import validate
from pydantic import TypeAdapter

from src.enums.global_enums import GlobalEnumMessages


class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get('Items')
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.model_validate(item)
        else:
            schema.parse_obj(self.response_json)
        return self


    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalEnumMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalEnumMessages.WRONG_STATUS_CODE.value
        return self
    
    #относится к response на Главной странице
    def assert_numbers_of_items(self):
        assert len(self.response_json) == 9, GlobalEnumMessages.WRONG_ELEMENTS_NUMBERS.value
        return self

