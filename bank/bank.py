def main():
    greet = input("Greeting: ").lower()
    print(check_hello(greet))




def check_hello(greeting):
    if greeting.find("hello") == 0:
        return "$0"
    elif greeting.split()[0][0]== "h":
        print(greeting[0][0])
        return "$20"
    else:
        return "$100"


main()