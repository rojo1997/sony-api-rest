from typing import List
from pydantic import BaseModel, Field, validator

class Geometry(BaseModel):
    type: str = Field(
        default = "Point"
    )
    coordinates: List[float]

    @validator("coordinates")
    def validateCoordinates(cls, v):
        if len(v) != 2:
            raise ValueError("invalid coordinate dimension")
        if v[0] > 180.0 or v[0] < -180.0:
            raise ValueError("invalid longitude value: " + str(v[0]))
        if v[1] > 90.0 or v[1] < -90.0:
            raise ValueError("invalid latitude value: " + str(v[1]))
        return v