def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    amount_of_meal = float(d.removeprefix('$'))
    return amount_of_meal


def percent_to_float(p):
    percent_value = p.removesuffix('%')
    percent = float(percent_value)/100
    return percent

main()