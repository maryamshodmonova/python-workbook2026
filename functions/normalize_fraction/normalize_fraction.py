def normalize_fraction(numerator, denominator):
    for i in range(min(abs(numerator), abs(denominator)), 0, -1):
        if numerator % i == 0 and denominator % i == 0:
            return (numerator // i, denominator // i)

    return (0, 1)


print(normalize_fraction(4, 8))
