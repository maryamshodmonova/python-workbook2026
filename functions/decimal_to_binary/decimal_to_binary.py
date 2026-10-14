def decimal_to_binary(n):
    if n == 0:
        return "0"

    result = ""

    while n > 0:
        remainder = n % 2
        result = str(remainder) + result
        n = n // 2

    return result