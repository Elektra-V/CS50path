def main():
    x, y, z = input("Expression: ").split(" ")
    check_math(x, y, z)


def check_math(first, op, second):
    if op == "+":
        add = float(first) + float(second)
        print(f"{add:.1f}")
    elif op == "-":
        sub = float(first) - float(second)
        print(f"{sub:.1f}")
    elif op == "*":
        prod = float(first) * float(second)
        print(f"{prod:.1f}")
    elif op == "/":
        div = float(first) / float(second)
        print(f"{div:.1f}")


main()