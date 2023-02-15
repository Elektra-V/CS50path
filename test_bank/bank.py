def main():

    greet = input("Greeting: ")
    print(value(greet))


def value(greeting : str) -> str:

    greeting = greeting.strip().lower()

    if "hello" in greeting:
        return "$0"

    elif greeting.startswith("h"):
        return "$20"

    else:
        return "$100"


if __name__ == "__main__":
    main()