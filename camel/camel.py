def main():

    camel_case = input("camelCase: ")
    print(camel_to_snake(camel_case))


def camel_to_snake(name: str) -> str :

    snake_case = ""

    for letter in name:

        if letter.isupper():
            snake_case += "_"

        snake_case += letter.lower()
        
    return f"snake_case: {snake_case}"


if __name__ == "__main__":
    main()