from app.core.db import db


class ParticipantRepository:
    def add_participant(self, participant_data: dict) -> dict:
        participant = participant_data.copy()
        participant["id"] = db.participant_id_counter
        db.participant_id_counter += 1
        db.participants.append(participant)
        return participant

    def get_participant_by_id(self, participant_id: int) -> dict | None:
        for participant in db.participants:
            if participant["id"] == participant_id:
                return participant
        return None

    def find_by_email(self, email: str) -> dict | None:
        for participant in db.participants:
            if participant["email"].lower() == email.lower():
                return participant
        return None

    def count_by_event_id(self, event_id: int) -> int:
        return sum(1 for participant in db.participants if participant["event_id"] == event_id)
