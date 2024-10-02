import random
import string


def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    # Define the character sets based on user preferences
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    # Ensure there's at least one character type selected
    if not characters:
        raise ValueError("At least one character type must be selected")

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    # Prompt the user for password preferences
    length = int(input("Enter the desired length for the password: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

    # Generate the password
    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        # Display the generated password
        print("Generated Password:", password)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
