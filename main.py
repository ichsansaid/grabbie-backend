from domain.usecases.grabbie_ucase_impl import GrabbieUcaseImpl
from infra.fastapi.delivery.grabbie_delivery import GrabbieDelivery
from infra.fastapi.provider.app_provider import app_provider
from infra.fastapi.routers.grabbie_router import new_grabbie_router
from infra.openapi.adapter.open_api_adapter import OpenAPIAdapter
from infra.openapi.config.open_api_config import OpenAPIConfig

app = app_provider()
new_grabbie_router(app, GrabbieDelivery(
    usecase=GrabbieUcaseImpl(
        open_api=OpenAPIAdapter(
            open_api_config=OpenAPIConfig(
                _env_file='.env',
                _env_file_encoding='utf-8'
            )
        )
    )
))