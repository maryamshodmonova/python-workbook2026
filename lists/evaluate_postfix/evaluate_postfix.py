def evaluate_postfix(tokens: list[str]) -> float:
    stack = []

    for token in tokens:

        # If token is a number
        if token.isdigit():
            stack.append(float(token))
        # If token is an operator
        else:
            if token == "~":
                number = stack.pop()
                stack.append(-number)

            else:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(a / b)
                elif token == "^":
                    stack.append(a ** b)
    return stack.pop()
print(evaluate_postfix(['3', '5', '2', '*', '+']))
    