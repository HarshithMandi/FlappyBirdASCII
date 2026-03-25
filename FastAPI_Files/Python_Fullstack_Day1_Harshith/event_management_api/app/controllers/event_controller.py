from fastapi import APIRouter, Depends, HTTPException, Query

from app.dependencies.service_dependency import get_event_service
from app.schemas.event_schema import EventCreate, EventResponse
from app.services.event_service import EventService

router = APIRouter(prefix="/events", tags=["events"])


@router.post("", response_model=EventResponse, status_code=201)
def create_event(
    payload: EventCreate,
    service: EventService = Depends(get_event_service),
) -> EventResponse:
    try:
        return service.create_event(payload)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@router.get("", response_model=list[EventResponse])
def list_events(
    location: str | None = Query(default=None, min_length=2),
    service: EventService = Depends(get_event_service),
) -> list[EventResponse]:
    return service.list_events(location=location)


@router.get("/{event_id}", response_model=EventResponse)
def get_event(
    event_id: int,
    service: EventService = Depends(get_event_service),
) -> EventResponse:
    try:
        return service.get_event(event_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
