from fastapi import FastAPI

from app.controllers.event_controller import router as event_router
from app.controllers.participant_controller import router as participant_router
from cors_middleware import add_cors_middleware

app = FastAPI(title="Event Management API", version="1.0")

add_cors_middleware(app)

app.include_router(event_router)
app.include_router(participant_router)


@app.get("/")
def health_check() -> dict:
    return {"status": "ok"}
