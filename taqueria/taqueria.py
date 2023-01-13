#prompting them item per line 
def main():
    total_bill()
    

def total_bill():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total_bill = 0
    while True:
        try:
            # take order from the user
            # convert each input into lowercase
            order_item = input("Item: ").title()
            # check if order is in items
            if order_item in menu.keys():
            # add the cost of the item to total bill
                total_bill += menu[order_item]
            # format the total bill output
            print(f"Total Bill: ${total_bill:.2f}")
        #catch when control-d is pressed
        except EOFError:
            break
        # catch if the item is not there
        except KeyError:
            pass


main()