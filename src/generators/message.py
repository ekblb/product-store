from .fakes import EmailFake


class Message:

    def __init__(self):
        self.result = {}
        self.reset()

    def set_email(self):
        self.result['email'] = EmailFake().build()
        return self

    def set_name(self):
        name = 'test_name'
        self.result['name'] = name
        return self

    def set_text(self, text='test_message'):
        self.result['text'] = text
        return self

    def reset(self):
        self.set_email()
        self.set_name()
        self.set_text()
        return self

    def build(self):
        return self.result
