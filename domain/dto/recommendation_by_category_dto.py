from pydantic import BaseModel


class RecommendationByCategoryDTO(BaseModel):
    category: str
    current_location: str