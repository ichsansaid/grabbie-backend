from fastapi import FastAPI


def app_provider() -> FastAPI:
    return FastAPI(
        description="Grabbie Backend"
    )