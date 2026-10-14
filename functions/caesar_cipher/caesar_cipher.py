def caesar_cipher(text, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for char in text:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            new_char = alphabet[(index + shift) % 26]
            if char.isupper():
                new_char = new_char.upper()
            result += new_char
        else:
            result += char
    return result
print(caesar_cipher("abc", 1))