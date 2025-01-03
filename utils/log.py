import inspect


def debug(message: str) -> None:
    print(f"[DEBUG] [{inspect.stack()[1][3]}] {message}")
