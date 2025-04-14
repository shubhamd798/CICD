# tests/test_main.py

from app.main import greet

def test_valid_greeting():
    assert greet("Shubh") == "Hello, Shubh!"

def test_invalid_greeting():
    assert greet("") == "Invalid name."
