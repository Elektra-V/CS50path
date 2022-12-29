def main():
    x, y, z = input("Expression: ").split(" ")
    result = check_math(float(x), y, float(z))
    print(result)


def check_math(first : float, op, second : float) -> str:
    if op == "+":
        add = first + second
        return f"{add:.1f}"

    elif op == "-":
        sub = first - second
        return f"{sub:.1f}"

    elif op == "*":
        prod = first * second
        return f"{prod:.1f}"

    elif op == "/":
        div = first / second
        return f"{div:.1f}"


if __name__ == "__main__":
    main()

