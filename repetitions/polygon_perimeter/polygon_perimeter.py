import math

x1 = float(input())
y1 = float(input())

first_x = x1
first_y = y1

perimeter = 0

x2 = input()

while x2 != "":
    x2 = float(x2)
    y2 = float(input())

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    perimeter += distance

    x1 = x2
    y1 = y2

    x2 = input()

distance = math.sqrt((first_x - x1) ** 2 + (first_y - y1) ** 2)
perimeter += distance

print(f"The perimeter of that polygon is {perimeter}")