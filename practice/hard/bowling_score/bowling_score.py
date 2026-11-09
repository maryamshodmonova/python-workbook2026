def roll_value(rolls, i):
    roll = rolls [i]
    if roll == "X":
        return 10
    if roll == "-":
        return 0
    if roll == "/":
        return 10 - roll_value(rolls, i-1)
    return int (roll)

def score(rolls):
    total = 0
    i = 0
    for frame in range (10):
        if rolls [i] == "X":
            total += 10 + roll_value(rolls, i+1) + roll_value(rolls, i + 2)
            i += 1 
        elif rolls[ i + 1 ] == "/":
            total += 10 + roll_value(rolls, i + 2)
            i += 2
        else: 
            total += roll_value(rolls, i) + roll_value(rolls, i + 1)
            i += 2
    return total
def is_perfect_game(rolls):
    if score(rolls) == 300: 
        return True 
    else:
        return False

    




    












































