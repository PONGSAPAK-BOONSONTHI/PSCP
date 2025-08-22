"""Pro"""
def main():
    """Pro"""
    x = int(input())
    y = int(input())
    a = int(input())
    z = int(input())
    b = x - y
    if z >= x:
        result = a * (z - (b * (z // x)))
        print(result)
    else:
        print(z * a)
main()
