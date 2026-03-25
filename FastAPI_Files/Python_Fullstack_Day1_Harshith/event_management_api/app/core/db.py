from dotenv import load_dotenv

load_dotenv()


class InMemoryDB:
    def __init__(self) -> None:
        self.events = []
        self.participants = []
        self.event_id_counter = 1
        self.participant_id_counter = 1


db = InMemoryDB()
