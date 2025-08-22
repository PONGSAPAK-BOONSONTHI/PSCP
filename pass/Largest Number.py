'''Code'''
def main():
    """Heee"""
    num1 = input()
    num2 = input()
    num3 = input()
    a = num1 + num2 + num3
    b = num1 + num3 + num2
    c = num2 + num1 + num3
    d = num2 + num3 + num1
    e = num3 + num1 + num2
    f = num3 + num2 + num1
    masnum = a
    if b > masnum:
        masnum = b
    if c > masnum:
        masnum = c
    if d > masnum:
        masnum = d
    if e > masnum:
        masnum = e
    if f > masnum:
        masnum = f
    print(int(masnum))
main()
