class InMemoryStorage:
    def __init__(self) -> None:
        self.loans = []
        self.loan_id_counter = 1


torage = InMemoryStorage()


# Alias for consistent import name
storage = torage
