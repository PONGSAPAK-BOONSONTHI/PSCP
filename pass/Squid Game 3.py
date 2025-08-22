""""Squid Game 3"""
def main():
    """Squid Game 3"""
    t1 = 0
    t2 = 0
    for i in range(20):
    # for i in range(10):
        ac = int(input())
        if i < 10:
        # if i < 4:
            t1 += ac
        else:
            t2 += ac
    if t1 < t2:
        print("A")
    elif t1 > t2:
        print("B")
    else:
        print("AB")
main()
