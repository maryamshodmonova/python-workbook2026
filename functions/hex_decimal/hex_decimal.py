def hex_decimal(hex_str):
    digits = "0123456789ABCDEF"
    result = 0
    for char in hex_str.upper():
        result = result * 16 + digits.index(char)
    return result
print(hex_decimal("A"))