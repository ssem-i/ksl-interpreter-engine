from collections import deque

from ksl_interpreter_engine.schemas.frame import FrameMessage

WORD_WINDOW_SIZE = 30
SYMBOL_WINDOW_SIZE = 10


class FrameBuffer:

    def __init__(self):
        self._frames: deque[FrameMessage] = deque(
            maxlen=WORD_WINDOW_SIZE
        )

    def append(self, frame: FrameMessage) -> None:
        self._frames.append(frame)

    def size(self) -> int:
        return len(self._frames)

    def get_word_window(self) -> list[FrameMessage] | None:
        if self.size() < WORD_WINDOW_SIZE:
            return None

        return list(self._frames)

    def get_symbol_window(self) -> list[FrameMessage] | None:
        if self.size() < SYMBOL_WINDOW_SIZE:
            return None

        return list(self._frames)[-SYMBOL_WINDOW_SIZE:]

    def clear(self) -> None:
        self._frames.clear()