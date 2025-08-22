"""Sequence V"""
import math
def main():
    """Sequence V"""
    num = int(input())
    result = num
    for _ in range(math.ceil(num / 7)):
        for _ in range(7):
            if _ == 6:
                print(result)
            else:
                print(result, end=" ")
            result -= 1
            if not result:
                break
main()
