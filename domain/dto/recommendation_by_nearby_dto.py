from typing import Optional

from pydantic import BaseModel


class RecommendationByNearbyDTO(BaseModel):
    category: Optional[str]
    current_location: str
