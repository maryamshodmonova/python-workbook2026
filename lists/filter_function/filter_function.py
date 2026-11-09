from typing import Callable


def filter_list(l: list, condition: Callable) -> list:
    result = []

    for item in l:
        if condition(item):
            result.append(item)

    return result


if __name__ == "__main__":
    def is_even(x):
        return x % 2 == 0

    print(filter_list([11, 4, 7, 22, 9], is_even))

    def is_positive(x):
        return x > 0

    print(filter_list([-2, -1, 0, 1, 2], is_positive))
    