def two_list_sum(list1: list[int], list2: list[int]) -> list[int]:
    result = []

    for i in range(len(list1)):
        result.append(list1[i] + list2[i])

    return result


if __name__ == "__main__":
    # Test your function
    print(two_list_sum([2, 3, 5], [7, 11, 13]))  # [9, 14, 18]
    print(two_list_sum([10, 20], [5, 10]))       # [15, 30]