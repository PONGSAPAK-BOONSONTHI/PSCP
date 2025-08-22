"""Bubble Tea"""
def main():
    """Bubble Tea"""
    bb, typebb = input().split()
    tea , x, y = input().split()
    # print(bb)
    listbb = {"H": 5, "O": 3, "J": 2}
    listtea = (
        {1: 12, 2: 18, 3: 25} if tea == "R" else
        {1: 15, 2: 20, 3: 30} if tea == "T" else
        {1: 10, 2: 15, 3: 20} if tea == "M" else {0:0}
    )
    numbb = (listbb[bb] * int(typebb)) + (listtea[int(x)] * int(y))
    print(numbb)
main()
