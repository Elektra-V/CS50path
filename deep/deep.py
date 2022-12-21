def main():
    question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    if check(question):
        return "Yes"
    return "No"


def check(user_answer: str) -> bool:
    if user_answer == "42" or user_answer == "forty-two" or user_answer == "forty two":
        return True
    return False


if __name__ == "__main__":
    print(main())

