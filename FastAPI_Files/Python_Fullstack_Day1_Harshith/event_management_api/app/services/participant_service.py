from app.repositories.event_repository import EventRepository
from app.repositories.participant_repository import ParticipantRepository
from app.schemas.participant_schema import ParticipantCreate, ParticipantResponse


class ParticipantService:
    def __init__(
        self,
        participant_repository: ParticipantRepository,
        event_repository: EventRepository,
    ) -> None:
        self.participant_repository = participant_repository
        self.event_repository = event_repository

    def register_participant(self, payload: ParticipantCreate) -> ParticipantResponse:
        event = self.event_repository.get_event_by_id(payload.event_id)
        if event is None:
            raise ValueError("Event not found")

        if self.participant_repository.find_by_email(payload.email) is not None:
            raise ValueError("Email already registered")

        registered_count = self.participant_repository.count_by_event_id(
            payload.event_id
        )
        if registered_count >= event["capacity"]:
            raise ValueError("Event capacity reached")

        created = self.participant_repository.add_participant(payload.model_dump())
        return ParticipantResponse(**created)

    def get_participant(self, participant_id: int) -> ParticipantResponse:
        participant = self.participant_repository.get_participant_by_id(participant_id)
        if participant is None:
            raise ValueError("Participant not found")

        return ParticipantResponse(**participant)
