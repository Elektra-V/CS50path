#import re

def main():
    input_time = input("What time is it? ")
    if (7,0) <= convert(input_time) <= (8,60):
        print("breakfast time")
    elif (12,0) <= convert(input_time) <= (13,60):
         print("lunch time")
    elif (18,0) <= convert(input_time) <= (19,60):
        print("dinner time")


def convert(time):
    hours, minutes = time.split(':')
    return int(hours), int(minutes)


if __name__ == "__main__":
    main()