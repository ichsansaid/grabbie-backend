from abc import ABC, abstractmethod
from typing import List


class OpenAPIContract(ABC):
    @abstractmethod
    def prompting(self, messages: List) -> str:
        pass
