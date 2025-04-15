from src.enums.pyenums import PyEnum


class MessageFields(PyEnum):
    email = 'email'
    name = 'name'
    status = 'status'
    message = 'message'


class Status(PyEnum):
    received = 'received'
    canceled = 'canceled'
    blocked = 'blocked'
