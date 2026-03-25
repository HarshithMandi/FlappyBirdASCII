from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    eligibility_multiplier: int = 10


config = AppConfig()
