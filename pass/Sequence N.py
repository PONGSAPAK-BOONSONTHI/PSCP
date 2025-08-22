"""Sequence N"""
def main():
    """Sequence N"""
    num = int(input())
    gap_N = 0
    for i in range(num):
        gap_N += 1
        for j in range(num):
            if j in (0, num - 1):
                print("*",end="")
            elif i == j:
                print("*",end="")
            else:
                print(" ",end="")
        print()
# *  *
# ** *
# * **
# *  *
main()
