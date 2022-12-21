# import re

def main():
    input_time = input("What time is it? ")
    hours, minutes = convert(input_time)

    if (7, 0) <= (hours, minutes) <= (8, 60):
        print("breakfast time")

    elif (12, 0) <= (hours, minutes) <= (13, 60):
         print("lunch time")

    elif (18, 0) <= (hours, minutes) <= (19, 60):
        print("dinner time")


def convert(time: str) -> float:
    hours, minutes = time.split(':')
    return int(hours), int(minutes)


if __name__ == "__main__":
    main()

