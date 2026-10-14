password = input()

upper = False
lower = False
digit = False
special = False

for char in password:
    if char.isupper():
        upper = True
    elif char.islower():
        lower = True
    elif char.isdigit():
        digit = True
    elif char in "!@#$%^&*()_+-=[]{}|;:,.<>?":
        special = True

length = len(password) >= 8

count = 0

if upper:
    count += 1
if lower:
    count += 1
if digit:
    count += 1
if special:
    count += 1
if length:
    count += 1

if count == 1:
    print("Very Weak")
elif count == 2:
    print("Weak")
elif count == 3:
    print("Medium")
elif count == 4:
    print("Strong")
else:
    print("Very Strong")