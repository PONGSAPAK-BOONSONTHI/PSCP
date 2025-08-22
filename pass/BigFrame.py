""""BigFrame"""
def main():
    """"BigFrame"""
    text1 = input().strip()
    text2 = input().strip()
    text3 = input().strip()
    text4 = input().strip()
    text5 = input().strip()
    maxtext = max(len(text1), len(text2), len(text3), len(text4), len(text5))
    print("*" * (maxtext + 4))
    print("* " + text1 + " " * (maxtext - len(text1)) + " *")
    print("* " + text2 + " " * (maxtext - len(text2)) + " *")
    print("* " + text3 + " " * (maxtext - len(text3)) + " *")
    print("* " + text4 + " " * (maxtext - len(text4)) + " *")
    print("* " + text5 + " " * (maxtext - len(text5)) + " *")
    print("*" * (maxtext + 4))
main()
