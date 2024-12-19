import random
import string

def generate_random_password(length=12):
    # Define the characters to choose from
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly choose characters and join them into a string
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Generate and print a random password of length 12
random_password = generate_random_password()
print(f"Generated Random Password: {random_password}")
