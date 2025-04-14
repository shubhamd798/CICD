# pass_example.py

def greet(name: str) -> str:
    """Returns a greeting message if the name is valid."""
    if name and isinstance(name, str):
        return f"Hello, {name}!"
    return "Invalid name."


if __name__ == "__main__":
    print(greet("SonarCloud"))
