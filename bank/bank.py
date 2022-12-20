def main():
    greet = input("Greeting: ").lower()
    print(check_hello(greet))


def check_hello(greeting):
    if "hello" in greeting:
        return "$0"
    elif greeting.startswith("h"):
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()