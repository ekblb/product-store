from enum import Enum

class Cat(Enum):
    phone = 'phone'
    notebook = 'notebook'
    monitor = 'monitor'


class ItemErrors(Enum):
    WRONG_IMG = "Email doesn't containt extention .jpg"