current_streak = 0
max_streak = 0

result = input()

while result != "":
    result = int(result)

    if result == 1:
        current_streak += 1

        if current_streak > max_streak:
            max_streak = current_streak

    else:
        current_streak = 0

    result = input()

print(f"Maximum streak: {max_streak}")