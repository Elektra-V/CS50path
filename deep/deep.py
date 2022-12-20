def main():
    ques = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    if check(ques):
        print("Yes")
    else:
        print("No")


def check(user_answer: str) -> bool:
    if user_answer == "42" or user_answer == "forty-two" or user_answer == "forty two":
        return True
    return False


if __name__ == "__main__":
    main()