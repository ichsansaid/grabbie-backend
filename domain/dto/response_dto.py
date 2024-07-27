from typing import Any

from pydantic import BaseModel


class ResponseDTO(BaseModel):
    data: Any
    message: str
