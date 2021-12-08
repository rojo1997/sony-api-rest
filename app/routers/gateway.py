from fastapi import APIRouter, Query, HTTPException
from starlette.requests import Request

from core.APILayer import APILayer

from schema.schema import Geometry

router = APIRouter(
    prefix = "/gateway",
    tags = ["gateway"]
)

@router.post("/")
async def post_coordinate(
    request: Request,
    input: Geometry
) -> str:
    myAPILayer: APILayer = request.app.state.APILayer
    try:
        result = myAPILayer.predict(input)
    except Exception as e:
        raise HTTPException(
            status_code = 400,
            detail = str(e)
        )
    return result