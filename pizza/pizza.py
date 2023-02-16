import sys
import csv
from tabulate import tabulate


def main():
    
    check_arguements()
    menu_table()


def check_arguements():

    if len(sys.argv) == 1 :
        sys.exit("Too few command-line arguements")
    
    elif len(sys.argv) >= 3:
        sys.exit("Too many comman-line arguements")


def menu_table():
    
    filename = sys.argv[1].strip().split(".")
    file_ext = filename[-1]

    if file_ext != "csv":
        sys.exit("Not a csv file")
    
    else:

        try:

            with open(sys.argv[1]) as file:
                menu = csv.DictReader(file)
                print(tabulate(menu, headers="keys", tablefmt="grid"))
        
        except FileNotFoundError:
            sys.exit("File does not exist")


if __name__ == "__main__":
    main()