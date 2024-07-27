from domain.usecases import test_grabbie_ucase_impl
from infra.openapi.config.open_api_config import OpenAPIConfig

open_api = OpenAPIConfig(
    _env_file='.env',
    _env_file_encoding='utf-8'
)
test_grabbie_ucase_impl.test_grabbie_ucase_by_prompt(open_api)
test_grabbie_ucase_impl.test_grabbie_ucase_by_category(open_api)