def main():
    greet = input("Greeting: ").lower()
    print(check_hello(greet))


def check_hello(greeting: str) -> str:
    if "hello" in greeting:
        return "$0"

    if greeting[0] == "h":
        return "$20"

    return "$100"


if __name__ == "__main__":
    main()

