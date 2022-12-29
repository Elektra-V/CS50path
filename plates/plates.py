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

    number = ""
    for letter in s:
        
        if letter.isdigit():
            index = s.find(letter)
            number += s[index:]
            break
    print(number)

    # check if the plate ends with numbers and not start with zero
    if number.find("0") == 0:
        return False

    # check if no special characters[., ' ', !]
    for letter in s:
        if letter in special_characters:
            return False

    return True




main()