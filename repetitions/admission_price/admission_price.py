total = 0

age = input()

while age != "":
    age = int(age)

    if age <= 2:
        total += 0
    elif age <= 12:
        total += 14
    elif age >= 65:
        total += 18
    else:
        total += 23

    age = input()

print(f"${total:.2f}")