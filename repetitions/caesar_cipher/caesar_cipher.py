message = input()
shift = int(input())

result = ""

for char in message:
    if char.isupper():
        result += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
    elif char.islower():
        result += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
    else:
        result += char

print(result)