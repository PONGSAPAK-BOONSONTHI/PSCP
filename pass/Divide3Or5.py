"""Divide3Or5"""
def main():
    """Divide3Or5"""
    n = int(input())
    sums = 0
    for i in range(1, n + 1):
        if not i % 3 and not i % 5:
            sums += i
        elif not i % 3:
            sums += i
        elif not i % 5:
            sums += i
    print(sums)
main()
