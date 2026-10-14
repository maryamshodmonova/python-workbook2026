def password_strength(pwd):
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    lower = False
    upper = False
    digit = False
    symbol = False

    for char in pwd:
        if char.islower():
            lower = True
        elif char.isupper():
            upper = True
        elif char.isdigit():
            digit = True
        elif char in special:
            symbol = True

    types = lower + upper + digit + symbol

    if len(pwd) >= 12 and types >= 3:
        return "strong"
    elif len(pwd) >= 8 and types >= 2:
        return "medium"
    else:
        return "weak"


print(password_strength("abc"))