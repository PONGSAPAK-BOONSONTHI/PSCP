"""Digit v2"""
def main():
    """Digit v2"""
    num = input().split()
    # print(num)
    if len(num) >= 4:
        num.pop(0)
    # print(num)
    digit = 0
    for i in num:
        if i in "thousand":
            digit = 4
        elif i in "hundred":
            digit = 3
        elif i in ("ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", \
        "seventeen", "eighteen", "twenty", "thirty", "forty", "fifty", \
        "sixty", "seventy", "eighty", "ninety"):
            digit = 2
        else:
            digit = 1
        if digit:
            break
    print(digit)
main()
