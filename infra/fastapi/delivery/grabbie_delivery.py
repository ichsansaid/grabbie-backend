from dataclasses import dataclass

from domain.contracts.grabbie_ucase_contract import GrabbieUcaseContract
from domain.dto.recommendation_by_nearby_dto import RecommendationByNearbyDTO
from domain.dto.recommendation_by_prompt_dto import RecommendationByPromptDTO
from domain.dto.response_dto import ResponseDTO


@dataclass
class GrabbieDelivery:
    usecase: GrabbieUcaseContract

    def recommendation_by_prompt(self, dto: RecommendationByPromptDTO) -> ResponseDTO:
        return ResponseDTO(
            data=self.usecase.recommendation_by_prompt(dto),
            message="success"
        )

    def recommendation_by_nearby(self, dto: RecommendationByNearbyDTO) -> ResponseDTO:
        return ResponseDTO(
            data=self.usecase.recommendation_by_nearby(dto),
            message="success"
        )
