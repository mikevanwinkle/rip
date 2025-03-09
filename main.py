import starlette.requests
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse
from src.responses import ORJSONResponse


async def homepage(request):
    return JSONResponse({'hello': 'world'})


async def api(request: starlette.requests.Request):
    return ORJSONResponse({'api': 'hello'})


routes = [
    Route("/", endpoint=homepage),
    Route("/api", endpoint=api)
]

app = Starlette(debug=True, routes=routes)
