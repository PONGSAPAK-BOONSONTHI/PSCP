"""LineSorting"""
def main():
    """LineSorting"""
    list_text = []
    num = int(input())
    for _ in range(num):
        text = input()
        list_text.append(text)
    list_text.sort(key=len)
    for i in list_text:
        print(i)
main()
