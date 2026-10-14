import random
import string

def password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    result = ""

    for i in range(length):
        result += random.choice(characters)

    return result
print(password(8))