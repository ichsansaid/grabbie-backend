from pydantic_settings import BaseSettings


class OpenAPIConfig(BaseSettings):
    api_key: str
    model: str
