"""fiveX"""
def main():
    """fiveX"""
    num = int(input())
    for _ in range(1, num + 1):
        if _ % 5:
            print("*" if _ == num + 1 else "*",end="")
        else:
            print("X" if _ == num + 1 else "X",end="")
main()
