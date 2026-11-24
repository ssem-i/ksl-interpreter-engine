from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from pydantic import ValidationError

from ksl_interpreter_engine.schemas.frame import FrameMessage
from ksl_interpreter_engine.services.frame_buffer import FrameBuffer

router = APIRouter()


@router.websocket("/ws/recognition")
async def recognize(websocket: WebSocket):
    await websocket.accept()

    frame_buffer = FrameBuffer()

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

            frame_buffer.append(frame)

            await websocket.send_json({
                "type": "frame_received",
                "frame_id": frame.frame_id,
                 "buffer_size": frame_buffer.size(),
                "word_ready": frame_buffer.get_word_window() is not None,
                "symbol_ready": frame_buffer.get_symbol_window() is not None,
            })

    except WebSocketDisconnect:
        pass