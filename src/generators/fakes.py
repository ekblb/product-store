from faker import Faker


class EmailFake:

    def __init__(self):
        self.fake = Faker()
        self.result = {
            "email": self.fake.email()
        }

    def build(self):
        return self.result
