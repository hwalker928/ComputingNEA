from typing import Tuple


def check_valid_private_key_password(password: str) -> Tuple[bool, str | None]:
    if not password:
        return (False, "Password cannot be empty")

    # Check if the password is at least 12 characters long
    if len(password) < 12:
        return (False, "Password must be at least 12 characters long")

    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        return (False, "Password must contain at least one digit")

    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return (False, "Password must contain at least one lowercase letter")

    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return (False, "Password must contain at least one uppercase letter")

    # Check if the password contains at least one special character
    if not any(char in "!@#$%^&*()-+" for char in password):
        return (False, "Password must contain at least one special character")

    return (True, None)