def digit_sum(n):
    n = abs(n)
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    return total
print(digit_sum(123))