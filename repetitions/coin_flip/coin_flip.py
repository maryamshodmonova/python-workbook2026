import random

total_flips = 0

for simulation in range(10):
    previous = random.choice(["H", "T"])
    count = 1
    flips = 1

    print(previous, end=" ")

    while count < 3:
        current = random.choice(["H", "T"])
        print(current, end=" ")

        flips += 1

        if current == previous:
            count += 1
        else:
            count = 1

        previous = current

    print(f"({flips} flips)")
    total_flips += flips

average = total_flips / 10

print(f"On average, {average:.1f} flips were needed.")