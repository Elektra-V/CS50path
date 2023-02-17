import sys
import csv


def main():

    check_arguements()
    write_scourgify(read_scourgify())


def check_arguements():

    if len(sys.argv) == 2 :
        sys.exit("Too few command-line arguements")
    
    elif len(sys.argv) >= 4:
        sys.exit("Too many comman-line arguements")


def read_scourgify() -> list:
    students = []
    
    filename = sys.argv[1].strip().split(".")
    file_ext = filename[-1]

    if file_ext != "csv":
        sys.exit("Not a csv file")
    
    else:
        try:

            with open(sys.argv[1]) as file:
                info = csv.DictReader(file)
                for row in info:
                    students.append(row)
                
        except FileNotFoundError:
            sys.exit("File does not exist")
    
    return students


def write_scourgify(information : list):
   
    for students in information:
        last, first = students['name'].replace(" ","").split(",")

        with open(sys.argv[2], "a") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writerow({"first": first, "last": last, "house": students['house']})


if __name__ == "__main__":
    main()