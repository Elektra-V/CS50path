def main():
    file_name = input("File name: ").lower().split(".")
    print(tell_extension(file_name))


def tell_extension(file) -> str:
    extension = file[-1]
    if extension == "gif":
        return "image/gif"
    if extension == "jpg" or extension == "jpeg":
        return "image/jpeg"
    if extension == "png":
        return "image/png"
    if extension == "pdf":
        return "application/pdf"
    if extension == "txt":
        return "text/plain"
    if extension == "zip":
        return "application/zip"
    return "application/octet-stream"
    

if __name__ == "__main__":
    main()