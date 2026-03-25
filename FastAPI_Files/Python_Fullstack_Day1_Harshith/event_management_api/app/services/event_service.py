from app.repositories.event_repository import EventRepository
from app.schemas.event_schema import EventCreate, EventResponse


class EventService:
    def __init__(self, event_repository: EventRepository) -> None:
        self.event_repository = event_repository

    def create_event(self, payload: EventCreate) -> EventResponse:
        existing = self.event_repository.find_by_name(payload.name)
        if existing is not None:
            raise ValueError("Event name already exists")

        created = self.event_repository.add_event(payload.model_dump())
        return EventResponse(**created)

    def list_events(self, location: str | None = None) -> list[EventResponse]:
        if location:
            events = self.event_repository.filter_by_location(location)
        else:
            events = self.event_repository.list_events()

        return [EventResponse(**event) for event in events]

    def get_event(self, event_id: int) -> EventResponse:
        event = self.event_repository.get_event_by_id(event_id)
        if event is None:
            raise ValueError("Event not found")

        return EventResponse(**event)
