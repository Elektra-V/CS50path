def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    
    first_letters = s[0:2]
    special_characters = ['.', ' ', '!', '-', '_', '?']
    print(first_letters)
    # check the length of the string
    if len(s) not in range(2,7):
        return False
    
    # check the plate has at least first two letters
    if not first_letters.isalpha():
        return False

    index = ""

    # check if the plate ends with numbers
    for letter in s:

        if letter.isdigit():
            # first number in original string
            index = s.find(letter)

            # check if every char after first num is num
            for char in s[index:]:
                if not char.isdigit():
                    # There is a letter after num
                    return False

            break

    # check if first number in original string is not zero
    if s.find("0") == index:
        return False

    # check if no special characters[., ' ', !]
    for letter in s:
        if letter in special_characters:
            return False

    return True




main()
