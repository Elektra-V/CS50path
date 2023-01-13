def main():
    while True:
        num, denom = input("Fraction: ").split("/")
        try:
            x = fuel_check(int(num), int(denom))
        except ValueError:
            continue

        print(x)


def fuel_check(num: int, denom: int) -> float:
    try:
        percentage = num / denom * 100

        if num < denom:

            if percentage >= 99:
                return "F"

            if percentage <= 1:
                return "E"
        else:
            raise e

    except ValueError:
        pass

    except ZeroDivisionError:
        pass

    except Exception as e:
        pass

    else:
        return percentage


main()

