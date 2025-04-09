from pydantic import BaseModel, PositiveFloat, PositiveInt, Field, field_validator
from typing import Literal

from src.enums.item_enums import Cat, ItemErrors


class Item(BaseModel):
    id : PositiveInt
    cat:  Cat
    desc: str = Field(max_length=1000)
    price: PositiveFloat
    title: str = Field(max_length=100)
    img: str
    
    @field_validator('img')
    def check_img_extention(cls, img):
        if '.jpg' in img:
            return img
        else:
            raise ValueError(ItemErrors.WRONG_IMG)



