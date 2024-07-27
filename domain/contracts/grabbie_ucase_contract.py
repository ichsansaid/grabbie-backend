from abc import ABC, abstractmethod

from domain.dao.item_place_dao import ListItemPlaceDAO
from domain.dto.recommendation_by_category_dto import RecommendationByCategoryDTO
from domain.dto.recommendation_by_prompt_dto import RecommendationByPromptDTO


class GrabbieUcaseContract(ABC):
    @abstractmethod
    def recommendation_by_category(self, dto: RecommendationByCategoryDTO) -> ListItemPlaceDAO:
        pass

    @abstractmethod
    def recommendation_by_prompt(self, dto: RecommendationByPromptDTO) -> ListItemPlaceDAO:
        pass