from typing import Annotated, Literal

from pydantic import BaseModel, Field

Landmark = tuple[float, float, float]

HandLandmarks = Annotated[
    list[Landmark],
    Field(min_length=21, max_length=21),
]


class FrameMessage(BaseModel):
    type: Literal["frame"]
    frame_id: int = Field(ge=0)
    timestamp_ms: int = Field(ge=0)
    nose: Landmark | None
    left_hand: HandLandmarks | None
    right_hand: HandLandmarks | None