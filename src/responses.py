import typing
from starlette.responses import Response
from starlette.background import BackgroundTask
import orjson

class ORJSONResponse(Response):
    media_type = "application/json"

    def __init__(
            self,
            content: typing.Any,
            status_code: int = 200,
            headers: typing.Mapping[str, str] | None = None,
            media_type: str | None = None,
            background: BackgroundTask | None = None,
    ) -> None:
        super().__init__(content, status_code, headers, media_type, background)

    def render(self, content: typing.Any) -> bytes:
        return orjson.dumps(
            content,
            option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY,
        )
