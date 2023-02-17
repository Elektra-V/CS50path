import sys
from PIL import Image, ImageOps


def main():
    # call the functions
    check_arguements()
    validate_arguements()
    wear_shirt()


def check_arguements():
    # check the minimum length of arguements in command line
    if len(sys.argv) <= 2 :
        sys.exit("Too few command-line arguements")
    # check the maximum length of arguements in command line
    elif len(sys.argv) >= 4:
        sys.exit("Too many comman-line arguements")


def validate_arguements():
    # create an empty list to store extensions of all cli arguements
    extension = []
    # loop over each cli arguements and extract extensions of file
    for arg in sys.argv[1:]:
        # extraction of extension
        filename = arg.strip().split(".")
        file_ext = filename[-1]
        # checking if file has extension as jpeg, jpg, png
        if file_ext not in ["jpeg", "jpg", "png"]:
            sys.exit("Invalid input")
        else:
            # add extensions of file to empty list so it becomes easy later
            extension.append(file_ext)
    # check if input and output have same extensions
    if extension[0] != extension[1]:
        sys.exit("Input and output have different extensions")


def wear_shirt():
    # open the images   
    shirt = Image.open("shirt.png")
    photo = Image.open(sys.argv[1])
    # resize and fit the image and save the dimensions as tuple
    a, b = shirt.size  
    photo = ImageOps.fit(photo, (a, b))
    # paste the shirt on muppets where mask value is shirt as well 
    photo.paste(shirt, box=None, mask=shirt)
    photo.save(sys.argv[2])


if __name__ == "__main__":
    main()