from models.user import User


class PremiumUser(User):
    def __init__(self, name: str, discount_rate: float = 0.10) -> None:
        super().__init__(name)
        self.discount_rate = discount_rate

    def get_discounted_total(self, total: float) -> float:
        return round(total * (1 - self.discount_rate), 2)
