"""Calculator"""
def main():
    """"Calculator"""
    num = int(input())
    if num != 1:
        s = 0
        for i in range(1, num + 1):
            s += len(str(i))
        print(num + s)
    else:
        print(num)
main()
