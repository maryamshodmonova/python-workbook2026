def binary_search(items: list, target) -> int:
    left = 0
    right = len(items) - 1

    while left <= right:
        middle = (left + right) // 2

        if items[middle] == target:
            return middle

        elif items[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return -1


if __name__ == "__main__":
    # Test your function
    items = [2, 3, 5, 7, 11]
    print(binary_search(items, 5))  # 2
    print(binary_search(items, 4))  # -1
    