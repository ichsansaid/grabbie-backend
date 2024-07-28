import json
from typing import List, Self, Optional

from pydantic import BaseModel


class ItemPlaceDAO(BaseModel):
    name: str
    category: str
    rating: float
    review: str
    starting_price: Optional[str]
    image_url: str


class ListItemPlaceDAO(List[ItemPlaceDAO]):
    @classmethod
    def model_validate(cls, value: str) -> Self:
        result: Self = []
        if isinstance(value, str):
            obj = json.loads(value)
            for o in obj:
                result.append(ItemPlaceDAO.model_validate(o))
        return result
