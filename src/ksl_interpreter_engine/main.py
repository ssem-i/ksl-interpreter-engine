from fastapi import FastAPI
from ksl_interpreter_engine.api.health import router as health_router
from ksl_interpreter_engine.api.recognition import router as recognition_router
app = FastAPI(
    title="KSL Interpreter Engine",
    version="0.1.0"
)

app.include_router(health_router)
app.include_router(recognition_router)