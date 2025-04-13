from .fakes import EmailFake, NameFake, TextFake


class Message:

    def __init__(self):
        self.result = {}
        self.reset()

    def set_email(self, email='test_mail'):
        email = EmailFake().build()
        self.result['email'] = email
        return self

    def set_name(self, name='test_name'):
        name = NameFake().build()
        self.result['name'] = name
        return self

    def set_text(self, text='test_text'):
        text = TextFake().build()
        self.result['text'] = text
        return self

    def reset(self):
        self.set_email()
        self.set_name()
        self.set_text()
        return self

    def build(self):
        return self.result
