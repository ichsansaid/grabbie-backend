from pydantic import BaseModel


class RecommendationByPromptDTO(BaseModel):
    user_prompt: str
