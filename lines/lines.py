import sys

def main():
    
    check_arguements()
    print(count_lines())


def check_arguements():

    if len(sys.argv) == 1 :
        sys.exit("Too few command-line arguements")
    
    elif len(sys.argv) >= 3:
        sys.exit("Too many comman-line arguements")


def count_lines():
    
    filename = sys.argv[1].strip().split(".")
    file_ext = filename[-1]

    if file_ext != "py":
        sys.exit("Not a python file")
    
    else:
        count = 0
        try:

            with open(filename) as file:
                lines = file.readlines()

                for line in lines:
                    
                    if line.startswith("#") or line.isspace():
                        count = count

                    else:
                        count +=1
        
        except FileNotFoundError:
            sys.exit("File does not exist")
    
        return count


if __name__ == "__main__":
    main()