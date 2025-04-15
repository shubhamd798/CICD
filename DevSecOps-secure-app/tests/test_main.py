from app.main import greet
from app.utils import format_message, is_valid_name

def test_greet_valid():
    assert greet("DevSecOps") == "Hello, DevSecOps!"

def test_greet_invalid():
    assert greet("") == "Invalid name."

def test_format_message():
    assert format_message("Shubham") == "Hello, Shubham!"

def test_is_valid_name():
    assert is_valid_name("Shubham") is True
    assert is_valid_name(" ") is False
