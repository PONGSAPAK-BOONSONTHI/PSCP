"""Seven"""
def main():
    """Seven"""
    num = str(input())
    nnum = len(num)
    num = int(num[-1])
    if nnum > 1:
        if num > 4:
            num = num // 4
        if num == 1:
            print(7)
        if num == 2 or num == 0:
            print(9)
        if num == 3:
            print(3)
        if num == 4:
            print(1)
    else:
        if num > 4:
            num = num // 4
        if num == 0:
            print(1)
        if num == 1:
            print(7)
        if num == 2:
            print(9)
        if num == 3:
            print(3)
        if num == 4:
            print(1)
main()
