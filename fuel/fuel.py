def main():
    x = fuel_check()
    print(x)

    
def fuel_check() -> float:
    while True:

        fraction_fuel = input("Fraction: ")
        part_1, part_2 = fraction_fuel.split("/")
        num, denom = int(part_1), int(part_2)
       
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