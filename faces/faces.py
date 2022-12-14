def main():
    message = convert(input("Type your message: "))
    
def convert(message):
    replace_emoticon = message.replace(":)", "🙂").replace(":(", "🙁")
    print(replace_emoticon)

main()