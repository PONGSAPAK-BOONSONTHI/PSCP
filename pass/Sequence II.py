"""Sequence II"""
def main():
    """Sequence II"""
    num = int(input())
    for i in range(num):
        rc = i
        for _ in range(num):
            if _ == num - 1:
                print(rc)
            else:
                print(rc, end=" ")
            rc += num
main()
