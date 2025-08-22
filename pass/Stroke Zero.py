"""Stroke Zero"""
def main():
    """Stroke Zero"""
    N = int(input())
    for i in range(N):
        for _ in range(i + 1):
            if _ in (0, i,) or i == N - 1:
                if _ == i:
                    print(0)
                else:
                    print(0,end=" ")
            else:
                if _ == i:
                    print(1)
                else:
                    print(1,end=" ")
main()
