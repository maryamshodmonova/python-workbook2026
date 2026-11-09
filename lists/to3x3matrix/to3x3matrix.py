def to3x3matrix(string: str) -> list[list[int]]:
    numbers = [int(x) for x in string.split()]

    matrix = [
        numbers[0:3],
        numbers[3:6],
        numbers[6:9]
    ]

    return matrix


if __name__ == "__main__":
    # Test your function
    matrix = to3x3matrix("2 3 5 7 11 13 17 19 23")

    for row in matrix:
        print(row)
        