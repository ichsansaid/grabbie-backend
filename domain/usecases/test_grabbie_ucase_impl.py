from domain.dto.recommendation_by_nearby_dto import RecommendationByNearbyDTO
from domain.dto.recommendation_by_prompt_dto import RecommendationByPromptDTO
from domain.usecases.grabbie_ucase_impl import GrabbieUcaseImpl
from infra.openapi.adapter.open_api_adapter import OpenAPIAdapter
from infra.openapi.config.open_api_config import OpenAPIConfig


def test_grabbie_ucase_by_prompt(open_api_config: OpenAPIConfig):
    grabbie = GrabbieUcaseImpl(
        open_api=OpenAPIAdapter(
            open_api_config=open_api_config
        )
    )
    result = grabbie.recommendation_by_prompt(RecommendationByPromptDTO(
        user_prompt="Tolong kasih saya tempat makanan enak di Bogor"
    ))
    print(result)


def test_grabbie_ucase_by_category(open_api_config: OpenAPIConfig):
    grabbie = GrabbieUcaseImpl(
        open_api=OpenAPIAdapter(
            open_api_config=open_api_config
        )
    )
    result = grabbie.recommendation_by_nearby(RecommendationByNearbyDTO(
        current_location="Blok M",
        category="Museum"
    ))
    print(result)
