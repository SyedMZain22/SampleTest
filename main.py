import random
import string

def generate_random_password(length=12):
    # Define the characters to choose from
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly choose characters and join them into a string
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Generate a random password and save it to a file
random_password = generate_random_password()

# Save the random password to a file
with open('password_output.txt', 'w') as f:
    f.write(f"Generated Random Password: {random_password}")

print(f"Generated Random Password: {random_password}")
