import random 
import sys

def main():
    
    while True:

        try:

            level = int(input("Level: "))

            if level > 0 :
                random_num = random.randint(1,level)
                check_guess(random_num)
                sys.exit()
        
        except (TypeError, ValueError):
            continue


def check_guess(num):

    while True:

        try:

            guess = int(input("Guess: ")) 

            if guess < 0 :
                continue

            if guess > num :
                print("Too Large !!")
            
            elif guess < num :
                print("Too Small !!")
            
            else:
                print("Just right !!")
                sys.exit()

        except (TypeError, ValueError):
            continue


if __name__ == "__main__":
    main()