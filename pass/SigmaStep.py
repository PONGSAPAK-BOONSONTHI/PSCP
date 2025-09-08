"""SigmaStep"""
def main():
    """SigmaStep"""
    x = int(input())
    y = int(input())
    n = int(input())
    if x == y:
        print(x)
    if not n or (x > y and n > 0) or (x < y and n < 0):
        print("error")
    else:
        result = 0
        for i in range(x, y + (1 if n > 0 else -1), n):
            result += i
        print(result)
main()
