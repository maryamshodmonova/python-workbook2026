bits = input()

while bits != "":
    if len(bits) != 8:
        print("Error")
    else:
        ones = bits.count("1")

        if ones % 2 == 0:
            parity = 0
        else:
            parity = 1

        print(f"Parity bit: {parity}")

    bits = input()