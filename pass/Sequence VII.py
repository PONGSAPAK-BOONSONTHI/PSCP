"""Sequence VII"""
def main():
    """Sequence VII"""
    num = int(input())
    result = 0
    for _ in range(num):
        result += 1
        for _ in range(result):
            if _ == result - 1:
                print(_ + 1)
            else:
                print(_ + 1, end=" ")
    result = num
    for _ in range(num):
        result -= 1
        for _ in range(result):
            if _ == result - 1:
                print(_ + 1)
            else:
                print(_ + 1, end=" ")
main()
