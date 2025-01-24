from typing import Tuple
from . import consts

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


def check_valid_name(name: str) -> Tuple[bool, str | None]:
    # Check if no name was provided
    if not name:
        return (False, "Name cannot be empty")

    # Check if the name is at least 3 characters long
    if len(name) < 3:
        return (False, "Name must be at least 3 characters long")

    # Check if the name is no longer than 16 characters
    if len(name) > 16:
        return (False, "Name cannot be more than 16 characters long")

    # Check if the name contains anything but letters
    if not name.isalpha():
        return (False, "Name must only contain letters")

    return (True, None)

def check_valid_colour_option(colour_option: str) -> Tuple[bool, str | None]:
    # Check if no colour was provided
    if not colour_option:
        return (False, "Colour option cannot be empty")

    # Check if the colour is in the valid colours list
    if colour_option not in consts.COLOUR_OPTIONS:
        return (False, "Not a valid colour option")

    return (True, None)