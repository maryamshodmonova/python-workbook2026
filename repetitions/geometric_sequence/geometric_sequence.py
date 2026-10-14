start = float(input())
ratio = float(input())
count = int(input())

term = start

for i in range(count):
    print(f"{term:.9g}")
    term = term * ratio