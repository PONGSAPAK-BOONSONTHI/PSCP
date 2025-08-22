"""Run Length Encoding"""
def main():
    """Run Length Encoding"""
    text = input()
    chrF = text[0]
    i = 0
    num = 0
    result = ""
    while i < len(text):
        if text[i] == chrF:
            num += 1
        else:
            result += f"{num}{chrF}"
            chrF = text[i]
            num = 1
        i += 1
    result += f"{num}{chrF}"
    print(result)
main()
