from .fakes import EmailFake, NameFake
# from .text_language import TextLanguage

from src.base_classes.builder import Builder
from src.generators.text_language import TextLocalization


# self.result=
# {
# "email": "test@mail.ru",
# "name": "test_name",
# "status": "test_status",
# "message": {
#               "en": {"text": "text_message"},
#               "ru": {"text": "текст_сообщения"},
#            }


class Message(Builder):

    def __init__(self):
        super().__init__()
        self.reset()

    def set_email(self, email='test_mail'):
        email = EmailFake().build()
        self.result['email'] = email
        return self

    def set_name(self, name='test_name'):
        name = NameFake().build()
        self.result['name'] = name
        return self

    def set_status(self, status="test_status"):
        self.result['status'] = status
        return self

    def reset(self):
        self.set_email()
        self.set_name()
        self.set_status()
        self.result['message'] = {
              "en": TextLocalization('en_US').build(),
              "ru": TextLocalization('ru_RU').build()
        }
        return self
