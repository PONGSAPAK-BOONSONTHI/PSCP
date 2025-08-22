"""Sequence IV"""
def main():
    """Sequence IV"""
    num = int(input())
    rc = 1
    for _ in range(num):
        for _ in range(num):
            if _ == num - 1:
                print(rc)
            else:
                print(rc, end=" ")
            rc += 1
main()
