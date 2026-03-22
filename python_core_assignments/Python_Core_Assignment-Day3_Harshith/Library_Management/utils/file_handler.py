import csv
from pathlib import Path

from exceptions.custom_exceptions import DataFileNotFoundError


class FileHandler:
    @staticmethod
    def read_csv(file_path: Path) -> list[dict]:
        if not file_path.exists():
            raise DataFileNotFoundError(f"Data file not found: {file_path.name}")

        with file_path.open("r", encoding="utf-8", newline="") as file:
            return list(csv.DictReader(file))

    @staticmethod
    def write_csv(file_path: Path, fieldnames: list[str], rows: list[dict]) -> None:
        with file_path.open("w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
