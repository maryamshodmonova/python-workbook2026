def decimal_hex(n):
    digits = "0123456789ABCDEF"

    if n == 0:
        return "0"

    result = ""
    while n > 0:
        remainder = n % 16
        result = digits[remainder] + result
        n //= 16

    return result
print(decimal_hex(10))