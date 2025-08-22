"""Ball"""
def main():
    """Ball"""
    h = float(input())
    n = 0
    while True:
        h = h * (3/5)
        if h < 0.01:
            break
        n += 1
    print(n)
main()
