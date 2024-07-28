import json
import re
from dataclasses import dataclass

from domain.contracts.grabbie_ucase_contract import GrabbieUcaseContract
from domain.contracts.open_api_contract import OpenAPIContract
from domain.dao.item_place_dao import ListItemPlaceDAO, ItemPlaceDAO
from domain.dto.recommendation_by_nearby_dto import RecommendationByNearbyDTO
from domain.dto.recommendation_by_prompt_dto import RecommendationByPromptDTO


@dataclass
class GrabbieUcaseImpl(GrabbieUcaseContract):
    open_api: OpenAPIContract

    def recommendation_by_nearby(self, dto: RecommendationByNearbyDTO) -> ListItemPlaceDAO:
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
                'content': f'You need to provide the data with JSON Format with fields: {", ".join(attrs)}, and if there is a field like price u need to provide it, dont varies.'
            },
            {
                'role': 'user',
                'content': f'Find nearby places around {dto.current_location} with the given category: {dto.category}'
            }
        ])
        pattern = r'```json(.*?)```'
        matches = re.findall(pattern, response, re.DOTALL)
        if matches:
            response = matches[0].strip()
        else:
            raise Exception("Parsing prompt error")
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
                'content': f'You need to provide the data with JSON with Fields: {", ".join(attrs)}'
            },
            {
                'role': 'user',
                'content': dto.user_prompt
            }
        ])
        pattern = r'```json(.*?)```'
        matches = re.findall(pattern, response, re.DOTALL)
        if matches:
            response = matches[0].strip()
        else:
            raise Exception("Parsing prompt error")
        result = ListItemPlaceDAO.model_validate(response)
        return result
