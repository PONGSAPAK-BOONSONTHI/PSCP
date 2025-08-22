"""Kangaroo"""
def main():
    """Kangaroo"""
    a = int(input())
    b = int(input())
    c = int(input())
    n1 = abs(a - b) - 1
    n2 = abs(b - c) - 1
    print(n1 if n1 > n2 else n2)
main()
