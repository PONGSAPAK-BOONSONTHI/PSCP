"""Backward"""
def main():
    """Backward"""
    list_text = []
    while True:
        text = input()
        if text == "NULL":
            break
        list_text.append(text)
    for i in reversed(list_text):
        print(i)
main()
