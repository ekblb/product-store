from enum import Enum
from pyenums import PyEnum


class Cat(PyEnum):
    phone = 'phone'
    notebook = 'notebook'
    monitor = 'monitor'


class ItemErrors(Enum):
    WRONG_IMG = "Email doesn't containt extention .jpg"
