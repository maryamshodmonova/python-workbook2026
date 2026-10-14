first = input()

if first != "":
    minimum = int(first)
    maximum = int(first)

    value = input()

    while value != "":
        value = int(value)

        if value < minimum:
            minimum = value

        if value > maximum:
            maximum = value

        value = input()

    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")