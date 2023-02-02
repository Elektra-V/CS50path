import random
import sys

def main():

    user_level = get_level()
    score = 0
    count = 10

    while count != 0:

        num_list = generate_integer(user_level)
        num1 = num_list[0]
        num2 = num_list[1]
        attempts = 0

        while attempts != 3:

            try:

                user_answer= int(input(f"{num1} + {num2} = ").strip())
                if user_answer == (num1+num2):
                    score += 1
                    break
                
                else:

                    attempts += 1
                    print("EEE")
            
            except(TypeError, ValueError):

                attempts += 1
                print("EEE")

            if attempts == 3:
                print(f"{num1} + {num2} = {(num1+num2)}")
            
        count -= 1
    print(score)


def get_level() -> int:

    while True:

        try:

            level = int(input("Level: ").strip())
            if level in [1,2,3]:
                return level
        
        except(TypeError, ValueError):
            continue


def generate_integer(level):

        if level == 1 :
            return (random.randint(1,9), random.randint(1,9))
        
        elif level == 2 :
            return (random.randint(10,99), random.randint(10,99))
    
        elif level == 3 :
            return (random.randint(100,999), random.randint(100,999))

        else:
            sys.exit()
    

if __name__ == "__main__":
    main()