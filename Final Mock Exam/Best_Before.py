"""Best_Before"""
def main():
    """Best_Before"""
    n = int(input())
    dmy = False
    mdy = False
    bf = []
    for _ in range(n):
        bf.append(input())
    for i in bf:
        dm1 = int(i[0:2])
        dm2 = int(i[2:4])
        # print(dm1, dm2)
        if dm1 > 12:
            dmy = True
        if dm2 > 12:
            mdy = True
    if dmy and mdy:
        print("no clue")
    elif dmy:
        print("ddmmyy")
    elif mdy:
        print("mmddyy")
    else:
        print("no clue")
main()
