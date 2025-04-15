# app/main.py

from app.utils import format_message, is_valid_name

def greet(name):
    if is_valid_name(name):
        return format_message(name)
    return "Invalid name."

if __name__ == "__main__":
    print(greet("DevSecOps"))
