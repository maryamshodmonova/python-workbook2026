total = 0

price = input()

while price != "":
    total += float(price)
    price = input()

pennies = round(total * 100)
remainder = pennies % 5

if remainder < 2.5:
    cash = pennies - remainder
else:
    cash = pennies + (5 - remainder)

print(f"Total: ${total:.2f}")
print(f"Cash payment: ${cash / 100:.2f}")