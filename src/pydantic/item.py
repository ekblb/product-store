from pydantic import BaseModel, PositiveFloat, PositiveInt, Field
from typing import Literal


class Item(BaseModel):
    id : PositiveInt
    cat: Literal ['phone', 'notebook', 'monitor']
    desc: str = Field(max_length=1000)
    price: PositiveFloat
    title: str = Field(max_length=100)
