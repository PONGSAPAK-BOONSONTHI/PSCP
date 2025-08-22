""""Donut"""
def main():
    """Donut"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    price = 0
    donut = 0
    num = 0
    while True:
        if num == b:
            num = 0
            donut += c
        if donut >= d:
            break
        if num < b:
            donut += 1
            price += a
        num += 1
    print(price, donut)
main()
