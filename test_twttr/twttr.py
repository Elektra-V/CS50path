def main():
  user_input = input("Input: ").strip()
  print(shorten(user_input))


def shorten(word: str) -> str:

    vowels = ['a', 'e', 'i', 'o', 'u']
    new_msg = ''

    for letter in word:

        if letter.lower() in vowels:
            letter = ""

        new_msg += letter
  
    return f"{new_msg}"

  
if __name__ == "__main__":
  main()