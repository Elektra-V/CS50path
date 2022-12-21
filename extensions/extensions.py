def main():
    extension = input("File name: ").split(".")[-1]
    print(tell_extension(extension))


def tell_extension(extension):
    if extension == "gif":
        return "image/gif"

    if extension == "jpg" or extension == "jpeg":
        return("image/jpeg")

    elif file[-1] == "png":
        return("image/png")
    elif file[-1] == "pdf":
        return("application/pdf")
    elif file[-1] == "txt":
        return("text/plain")
    elif file[-1] == "zip":
        return("application/zip")
    else:
        return("application/octet-stream")


if __name__ == "__main__":
    main()
