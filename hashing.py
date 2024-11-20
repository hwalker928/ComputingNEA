import hashlib

def set_salt(salt: str) -> None:
    global SALT
    SALT = salt

def hash_password(password: str) -> str:
    return hashlib.sha256((password + SALT).encode()).hexdigest()

def check_password(password: str, hashed_password: str) -> bool:
    return hash_password(password) == hashed_password