from app.repositories.event_repository import EventRepository
from app.repositories.participant_repository import ParticipantRepository
from app.services.event_service import EventService
from app.services.participant_service import ParticipantService

_event_repository = EventRepository()
_participant_repository = ParticipantRepository()

_event_service = EventService(_event_repository)
_participant_service = ParticipantService(_participant_repository, _event_repository)


def get_event_service() -> EventService:
    return _event_service


def get_participant_service() -> ParticipantService:
    return _participant_service
