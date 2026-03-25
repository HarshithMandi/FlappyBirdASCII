from app.core.db import db


class EventRepository:
    def add_event(self, event_data: dict) -> dict:
        event = event_data.copy()
        event["id"] = db.event_id_counter
        db.event_id_counter += 1
        db.events.append(event)
        return event

    def list_events(self) -> list[dict]:
        return list(db.events)

    def get_event_by_id(self, event_id: int) -> dict | None:
        for event in db.events:
            if event["id"] == event_id:
                return event
        return None

    def find_by_name(self, name: str) -> dict | None:
        for event in db.events:
            if event["name"].lower() == name.lower():
                return event
        return None

    def filter_by_location(self, location: str) -> list[dict]:
        location_lower = location.lower()
        return [
            event for event in db.events if event["location"].lower() == location_lower
        ]
