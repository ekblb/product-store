# from .fakes import TextFake
from faker import Faker


class TextLocalization:

    def __init__(self, language):
        self.fake = Faker(language)
        self.result = {
            "text": self.fake.text()
        }

    def build(self):
        return self.result
