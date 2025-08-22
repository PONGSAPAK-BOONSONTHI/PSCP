"""Number Message"""
def main():
    """Number Message"""
    text = input().upper()
    result = ""
    i = 0
    while True:
        if i >= len(text):
            break
        if text[i] == "3":
            result += "E"
        elif text[i] == "4":
            result += "A"
        elif text[i] == "5":
            result += "S"
        elif text[i] == "0":
            result += "O"
        elif text[i].isalpha():
            result += text[i]
        elif text[i] == " ":
            result += text[i]
        elif text[i] == "1":
            two = text[i:i+2]
            if two == "12":
                result += "R"
                i += 1
            elif two == "13":
                result += "B"
                i += 1
            else:
                result += "I"
        i += 1
    print(result)
# main()

def main2():
    """main2"""
    text = input().upper() \
        .replace("13", "B") \
        .replace("12", "R") \
        .replace("3", "E") \
        .replace("4", "A") \
        .replace("5", "S") \
        .replace("0", "O")
    print(text)
main2()
