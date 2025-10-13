"""Giraffe"""
def main():
    """Giraffe"""
    n = int(input())
    giraffe = [int(input()) for i in range(n)]
    count = 0
    if len(giraffe) == 1:
        print(1)
    else:
        for i, j in enumerate(giraffe):
            if not i and n > 1 and j > giraffe[i + 1]:
                count += 1
            elif i == n - 1 and n > 1 and j > giraffe[i - 1]:
                count += 1
            elif 0 < i < n - 1 and giraffe[i - 1] < j > giraffe[i + 1]:
                count += 1
        print(count)
main()
