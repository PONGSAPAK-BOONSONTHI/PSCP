"""Sequence II"""
def main():
    """Sequence II"""
    num = int(input())
    rc = 2
    for _ in range(num):
        for _ in range(num):
            if _ == num - 1:
                print(rc + _)
            else:
                print(rc + _, end=" ")
        rc += 1
main()
