from typing import List

from pydantic import BaseModel


class ItemPlaceDAO(BaseModel):
    place_name: str
    category: str
    rating: float
    max_rating: int
    review: str


class ListItemPlaceDAO(List[ItemPlaceDAO]):
    pass
