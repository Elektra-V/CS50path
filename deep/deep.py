def main():
    ques = input("What is the Answerto the Great Question of Life, the Universe, and Everything? ")
    if check(ques):
        print("Yes")
    else:
        print("No")


def check(user_answer):
    if user_answer.strip() == "42" or user_answer.lower().strip() == "forty-two" or user_answer.lower().strip() == "forty two":
        return True
    else:
        return False


main()