import json
from dataclasses import dataclass

from domain.contracts.grabbie_ucase_contract import GrabbieUcaseContract
from domain.contracts.open_api_contract import OpenAPIContract
from domain.dao.item_place_dao import ListItemPlaceDAO, ItemPlaceDAO
from domain.dto.recommendation_by_category_dto import RecommendationByCategoryDTO
from domain.dto.recommendation_by_prompt_dto import RecommendationByPromptDTO


@dataclass
class GrabbieUcaseImpl(GrabbieUcaseContract):
    open_api: OpenAPIContract

    def recommendation_by_category(self, dto: RecommendationByCategoryDTO) -> ListItemPlaceDAO:
        attrs = list(ItemPlaceDAO.model_fields.keys())
        response = self.open_api.prompting([
            {
                'role': 'system',
                'content': 'You acted as a friendly and knowledgeable assistant, providing recommendations for places '
                           'to eat and visit in Indonesia. Your task is to suggest locations that offer unique '
                           'experiences, either through their food or cultural and natural attractions'
            },
            {
                'role': 'system',
                'content': f'You need to provide the data with JSON Format with fields: {", ".join(attrs)}'
            },
            {
                'role': 'user',
                'content': f'Find nearby places around {dto.current_location} with the given category: {dto.category}'
            }
        ])
        result = ListItemPlaceDAO.model_validate(response)
        return result

    def recommendation_by_prompt(self, dto: RecommendationByPromptDTO) -> ListItemPlaceDAO:
        attrs = list(ItemPlaceDAO.model_fields.keys())
        response = self.open_api.prompting([
            {
                'role': 'system',
                'content': 'You acted as a friendly and knowledgeable assistant, providing recommendations for places '
                           'to eat and visit in Indonesia. Your task is to suggest locations that offer unique '
                           'experiences, either through their food or cultural and natural attractions'
            },
            {
                'role': 'system',
                'content': f'You need to provide the data with JSON Format with fields: {", ".join(attrs)}'
            },
            {
                'role': 'user',
                'content': dto.user_prompt
            }
        ])
        result = ListItemPlaceDAO.model_validate(response)
        return result
