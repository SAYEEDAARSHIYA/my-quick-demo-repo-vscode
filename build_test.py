# hello_success.py

def greet(name):
    return f"Hello, {name}! This build will succeed."

if __name__ == "__main__":
    user = input("Enter your name: ")
    print(greet(user))
    exit(0)  # Success
