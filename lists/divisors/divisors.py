def list_divisors(n: int) -> list[int]:
    divisors = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    return divisors


if __name__ == "__main__":
    # Test your function
    print(list_divisors(12))   # [1, 2, 3, 4, 6, 12]
    print(list_divisors(7))    # [1, 7]
    print(list_divisors(1))    # [1]