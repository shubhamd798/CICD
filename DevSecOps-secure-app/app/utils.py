# # app/utils.py

# def format_message(name: str) -> str:
#     """
#     Formats a friendly greeting message.
#     """
#     return f"Hello, {name}!"

# def is_valid_name(name: str) -> bool:
#     """
#     Validates that the name is a non-empty string.
#     """
#     return isinstance(name, str) and len(name.strip()) > 0


import pytest
from app.main import greet
from app.utils import format_message, is_valid_name

def test_greet_valid_name():
    assert greet("Alice") == "Hello, Alice!"

def test_greet_invalid_name():
    assert greet("   ") == "Invalid name."

def test_format_message():
    assert format_message("Shubham") == "Hello, Shubham!"

def test_is_valid_name_true():
    assert is_valid_name("DevSecOps") is True

def test_is_valid_name_false_empty():
    assert is_valid_name("") is False

def test_is_valid_name_false_non_string():
    assert is_valid_name(1234) is False
