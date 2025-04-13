from faker import Faker


class Fake:

    def __init__(self):
        self.fake = Faker()
        self.result = {}

    def build(self):
        return self.result


class EmailFake(Fake):

    def __init__(self):
        super().__init__()
        self.result = self.fake.email()


class NameFake(Fake):

    def __init__(self):
        super().__init__()
        self.result = self.fake.name()


# class TextFake(Fake):

#     def __init__(self, lang):
#         super().__init__()
#         self.fake = Faker(lang)
#         self.result = self.fake.text()
