"""Left Arrow"""
def main():
    """Left Arrow"""
    k = int(input())
    n = int(input())
    gap = n // 2
    g = 0
    for i in range(n):
        print(" " * (gap - i),end="")
        if i > gap:
            g += 1
            print(" " * g,end="")
        for _ in range(k):
            print("*",end="")
        print()
main()
