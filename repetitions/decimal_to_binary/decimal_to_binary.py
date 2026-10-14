q = int(input())

if q == 0:
    result = "0"
else:
    result = ""

    while q > 0:
        r = q % 2
        result = str(r) + result
        q = q // 2

print(f"The binary equivalent is {result}")