from dataclasses import dataclass
from typing import List

import openai

from domain.contracts.open_api_contract import OpenAPIContract
from infra.open_api.config.open_api_config import OpenAPIConfig


@dataclass
class OpenAPIAdapter(OpenAPIContract):
    open_api_config: OpenAPIConfig

    def prompting(self, messages: List) -> str:
        response = openai.ChatCompletion.create(
            api_key=self.open_api_config.api_key,
            messages=messages,
            model=self.open_api_config.model,
            max_tokens=2500,
            temperature=0.1
        )
        response_message = response.choices[0].message.content
        return response_message
