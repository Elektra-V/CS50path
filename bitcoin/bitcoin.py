import requests
import sys
import json

def main():

    number = get_number()
    bitcoins_cost = total_cost(number)
    print(f"${bitcoins_cost:,.4f}")
    

def get_number() -> float:

    try:

        user_count = float(sys.argv[1])
        if user_count < 0 :
            sys.exit()
        
        return user_count
    
    except (ValueError, TypeError):
        sys.exit("Command-line argument is not a number")
    
    except IndexError:
        sys.exit("Missing command-line argument")


def total_cost(num) -> float:

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data_object = response.json()
    total_cost = data_object["bpi"]["USD"]["rate_float"] * num
    return total_cost


main()