"""Dart"""
def main():
    """Dart"""
    num = int(input())
    count = 0
    for _ in range(num):
        ps = input()
        ps = ps.split(" ")
        p_x = int(ps[0])
        p_y = int(ps[1])
        r = ((p_x**2)+(p_y**2))**0.5
        if r <= 2:
            count += 5
        elif r <= 4:
            count += 4
        elif r <= 6:
            count += 3
        elif r <= 8:
            count += 2
        elif r <= 10:
            count += 1
    print(count)
main()
