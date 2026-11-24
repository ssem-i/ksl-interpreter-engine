from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from pydantic import ValidationError

from ksl_interpreter_engine.schemas.frame import FrameMessage

router = APIRouter()


@router.websocket("/ws/recognition")
async def recognize(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            data = await websocket.receive_text()

            try:
                frame = FrameMessage.model_validate_json(data)
            except ValidationError:
                await websocket.send_json({
                    "type": "error",
                    "message": "Invalid frame data",
                })
                continue

            await websocket.send_json({
                "type": "frame_received",
                "frame_id": frame.frame_id,
            })

    except WebSocketDisconnect:
        pass