def tokenize_expression(expr: str) -> list[str]:
    tokens = []
    number = ""

    for char in expr:
        if char.isdigit():
            number += char

        elif char in "+-*/^()":
            if number:
                tokens.append(number)
                number = ""

            tokens.append(char)

        elif char == " ":
            continue

    if number:
        tokens.append(number)

    return tokens


if __name__ == "__main__":
    print(tokenize_expression("3+5*2"))
    print(tokenize_expression("(10+20)*3"))
    print(tokenize_expression("15 - 7 + 2"))