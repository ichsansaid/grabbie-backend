from fastapi import APIRouter, FastAPI

from infra.fastapi.delivery.grabbie_delivery import GrabbieDelivery


def new_grabbie_router(app: FastAPI, delivery: GrabbieDelivery):
    router = APIRouter(
        prefix="/recommendation"
    )
    router.post("/by_prompt")(delivery.recommendation_by_prompt)
    router.post("/by_nearby")(delivery.recommendation_by_nearby)
    app.include_router(router)
