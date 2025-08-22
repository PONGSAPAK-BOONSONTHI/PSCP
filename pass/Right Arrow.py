"""Right Arrow"""
def main():
    """Right Arrow"""
    k = int(input())
    n = int(input())
    gap = n // 2
    for i in range(n):
        if i < gap + 1:
            print(" " * i,end="")
            for _ in range(k):
                print("*",end="")
            gap_l = i
        else:
            gap_l -= 1
            print(" " * gap_l,end="")
            for _ in range(k):
                print("*",end="")
        print()
main()
