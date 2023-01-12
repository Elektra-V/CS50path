def main():
    user_input = input("Input: ")
    new_msg = omit_vowel(user_input)
    print(f"Output: {new_msg}")


def omit_vowel(msg: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    new_msg = ""

    for letter in msg:

        if letter.lower() in vowels:
            letter = ""

        new_msg += letter

    return new_msg


if __name__ == "__main__":
    main()

