from typing import Any, TypeVar, Generic

from pydantic import BaseModel

T = TypeVar('T')


class ResponseDTO(BaseModel, Generic[T]):
    data: T
    message: str
