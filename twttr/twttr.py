def main():
  user_input = input("Input: ")
  print(omit_vowel(user_input))


def omit_vowel(msg: str) -> str:
  msg = msg
  vowels = ['a', 'e', 'i', 'o', 'u']
  new_msg = ''

  for letter in msg:

    if letter.lower() in vowels:
      letter = ""

    new_msg += letter
  
  return f"Output: {new_msg}"

  
if __name__ == "__main__":
  main()