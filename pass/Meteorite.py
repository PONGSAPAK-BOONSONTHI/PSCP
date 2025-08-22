"""Meteorite"""
def main():
    """Meteorite"""
    a = float(input())
    b = int(input())
    c = float(input())
    loop = 0
    num = 0
    while True:
        size = a / (b ** loop)
        if size < c:
            break
        num += b ** loop
        loop += 1
    print(num)
main()
