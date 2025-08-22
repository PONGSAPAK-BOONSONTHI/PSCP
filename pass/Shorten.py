"""Shorten"""
def main():
    """Shorten"""
    n_old = 0
    F = True
    result = ""
    gap = False
    while True:
        n = int(input())
        if n == -1:
            break
        if not F:
            if n_old + 1 == n:
                gap = True
                n_old = n
                continue
            if gap:
                result += f"-{n_old}"
                n_old = n
            gap = False
            if not gap:
                n_old = n
                result += f", {n}"
        else:
            result += f"{n}"
            n_old = n
            F = False
            continue
    if gap:
        result += f"-{n_old}"
    print(result)
main()
