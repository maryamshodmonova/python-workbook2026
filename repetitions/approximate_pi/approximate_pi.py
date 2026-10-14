pi = 3.0
n = 2

print(f"Approximation 1: {pi}")

for i in range(2, 16):
    denominator = n * (n + 1) * (n + 2)
    term = 4 / denominator

    if i % 2 == 0:
        pi += term
    else:
        pi -= term

    print(f"Approximation {i}: {pi}")

    n += 2