import random

maximum = random.randint(1, 100)
print(maximum)

updates = 0

for i in range(99):
    number = random.randint(1, 100)

    if number > maximum:
        maximum = number
        updates += 1
        print(f"{number} <== Update")
    else:
        print(number)

print(f"The maximum value found was {maximum}")
print(f"The maximum value was updated {updates} times")