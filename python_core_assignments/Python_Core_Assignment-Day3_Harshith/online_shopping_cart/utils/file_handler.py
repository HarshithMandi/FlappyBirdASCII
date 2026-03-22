from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
ORDER_HISTORY_FILE = DATA_DIR / "order_history.txt"


def ensure_order_file() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not ORDER_HISTORY_FILE.exists():
        ORDER_HISTORY_FILE.write_text("", encoding="utf-8")


def save_order(user_name: str, cart_items: list[dict], total: float, file_path: Path | None = None) -> None:
    ensure_order_file()
    target = file_path or ORDER_HISTORY_FILE
    item_text = ", ".join([f"{item['name']} x{item['quantity']}" for item in cart_items])
    line = f"User: {user_name} | Items: {item_text} | Total: {total:.2f}\n"
    with target.open("a", encoding="utf-8") as file:
        file.write(line)


def read_order_history(file_path: Path | None = None) -> list[str]:
    ensure_order_file()
    target = file_path or ORDER_HISTORY_FILE
    return target.read_text(encoding="utf-8").splitlines()
