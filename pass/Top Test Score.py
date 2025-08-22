"""Top Test Score"""
def main():
    """Top Test Score"""
    n =  int(input())
    max_c = 0
    max_n = 0
    for _ in range(n):
        sc = int(input())
        if sc >= max_c:
            if max_c == sc:
                max_n += 1
            elif sc > max_c:
                max_c = sc
                max_n = 1
    print(max_c)
    print(max_n)
# main()

"""Top Test Score"""
def sos():
    """Top Test Score"""
    n =  int(input())
    max_c = 0
    max_n = 0
    for _ in range(n):
        sc = int(input())
        if sc >= max_c:
            if max_c == sc:
                max_n += 1
            else:
                max_n = 1
            max_c = sc
    print(max_c)
    print(max_n)
sos()
