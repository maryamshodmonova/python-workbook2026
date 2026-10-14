def to_base(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if n == 0:
        return "0"
    result = ""
    sign = ""
    if n < 0:
        n = -n
        sign = "-"
    while n > 0:
        remainder = n % base
        result = digits[remainder] + result
        n = n // base
    return sign + result
print(to_base(10, 2)) 