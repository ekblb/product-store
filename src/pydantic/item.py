from pydantic import BaseModel, PositiveFloat, PositiveInt, Field, field_validator
from typing import Literal

from src.enums.item_enums import Cat, ItemErrors

        # {
        #     "cat": "phone",
        #     "desc": "The Nokia Lumia 1520 is powered by 2.2GHz quad-core Qualcomm Snapdragon 800 processor and it comes with 2GB of RAM. ",
        #     "id": 2,
        #     "img": "imgs/Lumia_1520.jpg",
        #     "price": 820.0,
        #     "title": "Nokia lumia 1520"
        # },


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



