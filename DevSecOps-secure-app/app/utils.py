# app/utils.py

def format_message(name: str) -> str:
    """
    Formats a friendly greeting message.
    """
    return f"Hello, {name}!"

def is_valid_name(name: str) -> bool:
    """
    Validates that the name is a non-empty string.
    """
    return isinstance(name, str) and len(name.strip()) > 0
