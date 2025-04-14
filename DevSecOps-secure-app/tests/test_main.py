# import pytest
# from app.main import your_main_function  # adjust based on actual function

# def test_main_function_behavior():
#     result = your_main_function()  # use real input if needed
#     assert result == expected_output

import pytest
from app.main import greet

def test_greet_valid_name():
    result = greet("Alice")
    assert result == "Hello, Alice!"  # assuming this is what format_message returns

def test_greet_invalid_name():
    result = greet("123")
    assert result == "Invalid name."
