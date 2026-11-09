def to_matrix(numbers: list[int], rows: int, cols: int) -> list[list[int]]:
    matrix = []

    for i in range(rows):
        row = numbers[i * cols:(i + 1) * cols]
        matrix.append(row)

    return matrix


if __name__ == "__main__":
    # Test your function
    print(to_matrix([2, 3, 5, 7, 11, 13], 2, 3))
    # [[2, 3, 5], [7, 11, 13]]

    print(to_matrix([2, 3, 5, 7], 2, 2))
    # [[2, 3], [5, 7]]
    