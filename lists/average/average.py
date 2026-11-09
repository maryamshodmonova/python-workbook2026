def average(numbers: list[int]) -> float:
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)
if __name__ == "__main__":
   
    print(average([2, 3, 5, 7, 11]))  # 5.6
    