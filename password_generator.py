import secrets, string

def generate(length=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(alphabet) for _ in range(length))

if __name__ == "__main__":
    try:
        n = int(input("Password length: "))
        print(generate(max(4, n)))
    except ValueError:
        print("Please enter a number.")
