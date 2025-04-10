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
        error_message = GlobalEnumMessages.WRONG_STATUS_CODE.value

        if isinstance(status_code, list):
            assert self.response_status in status_code, error_message
        else:
            assert self.response_status == status_code, error_message
        return self

    # относится к response на Главной странице
    def assert_numbers_of_items(self):
        error_message = GlobalEnumMessages.WRONG_ELEMENTS_NUMBERS.value

        assert len(self.response_json) == 9, error_message
        return self
