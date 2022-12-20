def main():
    input_time = input("What time is it? ")
    if 7 <= convert(input_time) <= 8:
        print("breakfast time")
    elif 12 <= convert(input_time) <= 13:
         print("lunch time")
    elif 18 <= convert(input_time) <= 19:
        print("dinner time")


def convert(time: str) -> float:
    hours, minutes = time.split(':')
    hours = float(hours)
    minutes = float(minutes)
    float_time = hours + minutes/60
    return float_time


if __name__ == "__main__":
    main()