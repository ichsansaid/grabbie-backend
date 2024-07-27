import json
from typing import List, Self

from pydantic import BaseModel


class ItemPlaceDAO(BaseModel):
    place_name: str
    category: str
    rating: float
    max_rating: int
    review: str


class ListItemPlaceDAO(List[ItemPlaceDAO]):
    @classmethod
    def model_validate(cls, value: str) -> Self:
        result: Self = []
        if isinstance(value, str):
            obj = json.loads(value)
            for o in obj:
                result.append(ItemPlaceDAO.model_validate(o))
        return result