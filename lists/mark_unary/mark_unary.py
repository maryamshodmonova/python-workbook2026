def mark_unary(tokens: list[str]) -> list[str]:
    result = []

    for i in range(len(tokens)):
        if tokens[i] == "-":
            if i == 0 or tokens[i - 1] in "+-*/^(":
                result.append("~")
            else:
                result.append("-")
        else:
            result.append(tokens[i])

    return result


if __name__ == "__main__":
    print(mark_unary(['-', '5', '+', '3']))
    print(mark_unary(['(', '-', '5', ')', '*', '2']))
    print(mark_unary(['3', '-', '5']))