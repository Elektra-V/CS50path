def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    meal_cost = float(dollars.removeprefix('$'))
    return meal_cost


def percent_to_float(percent):
    percent_value = percent.removesuffix('%')
    percentage = float(percent_value) / 100
    return percentage


main()

