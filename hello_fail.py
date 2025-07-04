# hello_fail.py

def greet(name):
    return f"Hello, {name}! This build will fail."

if __name__ == "__main__":
    user = input("Enter your name: ")
    print(greet(user))
    exit(1)  # Failure
