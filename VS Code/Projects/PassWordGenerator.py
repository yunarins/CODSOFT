import random
import string

def generate_password(length=12, complexity='medium'):
    if complexity == 'low':
        characters = string.ascii_lowercase + string.digits
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits
    elif complexity == 'high':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Complexity level should be 'low', 'medium', or 'high'.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    
    try:
        length = int(input("Enter the desired length of the password: "))

        complexity = input("Enter the complexity level of the password (low/medium/high): ").lower()
        # Generate and print the password
        password = generate_password(length, complexity)
        print("Generated password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid length (integer) for the password.")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
