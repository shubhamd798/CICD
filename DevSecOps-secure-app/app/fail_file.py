# fail_example.py

import os

def greet(name):
    return "Hello " + name  # ➤ Missing type hint, poor string formatting

def unused_function():  # ➤ Unused code
    return os.getenv("SECRET_KEY")  # ➤ Potential secret exposure

if __name__ == "__main__":
    print(greet("SonarCloud"))
