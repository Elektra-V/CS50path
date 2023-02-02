import emoji

def main():
    emo = input("Input: ")
    print(emoji.emojize(f"Output: {emo} ", language='alias'))


main()