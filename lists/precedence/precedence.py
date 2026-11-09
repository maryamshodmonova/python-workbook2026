def precedence(operation: str) -> int:
    if operation in "+-":
        return 1
    elif operation in "*/":
        return 2
    elif operation == "^":
        return 3
    elif operation == "~":
        return 4
    else:
        return 0


if __name__ == "__main__":
    print(precedence('+'))  # 1
    