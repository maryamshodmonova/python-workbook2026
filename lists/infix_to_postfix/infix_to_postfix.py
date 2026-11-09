from lists.precedence.precedence import precedence


def infix_to_postfix(tokens: list[str]) -> list[str]:
    output = []
    stack = []

    for token in tokens:

        # 1. If token is a number, add it to output
        if token.isdigit():
            output.append(token)

        # 2. If token is an opening parenthesis
        elif token == "(":
            stack.append(token)

        # 3. If token is a closing parenthesis
        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())

            if stack:
                stack.pop()

        # 4. If token is an operator
        else:
            while (stack
                   and stack[-1] != "("
                   and precedence(stack[-1]) >= precedence(token)):
                output.append(stack.pop())

            stack.append(token)

    # 5. Move remaining operators to output
    while stack:
        output.append(stack.pop())

    return output


if __name__ == "__main__":
    print(infix_to_postfix(['3', '+', '5', '*', '2']))
  