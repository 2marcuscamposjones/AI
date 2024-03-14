# Programmer: Campos-Jones
# Date: 3.12.2024
# program: Password Generator
# Resource: https://youtu.be/jRAAaDll34Q?si=SZq8WSYzjrmuAoIA

import hashlib
import getpass

def hash_password(password, salt):
    # Combine password and salt, then hash using SHA-256
    hashed_password = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    return hashed_password

def main():
    # Get user input for the password without displaying characters
    password = getpass.getpass("Enter your password: ")

    # Generate a random salt (for simplicity, you can use a more secure method)
    salt = "somerandomsalt"

    # Hash the password with the salt
    hashed_password = hash_password(password, salt)

    # Print the hashed password
    print(f"Hashed Password: {hashed_password}")

if __name__ == "__main__":
    main()
