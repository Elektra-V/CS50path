def main():
    input_time = input("What time is it? ")
    time = convert(input_time)
    print(time)

    time = convert(input_time)

    if 7 <= time <= 8:
        print("breakfast time")

    if 12 <= time <= 13:
        print("lunch time")

    if 18 <= time <= 19:
        print("dinner time")


def convert(time: str) -> float:
    # 12 hour format
    if "a.m" in time or "p.m" in time:
        time, time_ext = time.split(" ")
        hour, minutes = time.split(":")

        if time_ext == "p.m" and hour != "12":
            hour = int(hour)
            hour += 12

        if time_ext == "a.m":
            hour = "00"

        hour = float(hour)
        minutes = float(minutes)
        return hour + (minutes / 60)

    # 24 hour format
    hours, minutes = time.split(':')
    hours = float(hours)
    minutes = float(minutes)
    float_time = hours + (minutes / 60)
    return float_time


if __name__ == "__main__":
    main()

