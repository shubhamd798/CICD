from app.main import greet  # ← importing your function from main.py

def test_greet_valid():
    assert greet("Shubham") == "Hello, Shubham!"  # success test

def test_greet_invalid():
    assert greet("") == "Invalid name."  # fail case test