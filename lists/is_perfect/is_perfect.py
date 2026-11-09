def is_perfect(n: int) -> bool:
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n


if __name__ == "__main__":
    # Test your function
    print(is_perfect(6))   # True
    print(is_perfect(28))  # True
    print(is_perfect(12))  # False
    