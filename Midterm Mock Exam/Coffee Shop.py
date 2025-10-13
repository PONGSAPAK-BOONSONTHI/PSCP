"""Coffee Shop"""
def main():
    """Coffee Shop"""
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = int(input())
    n1 = a + ((a - (a * (b / 100))) * (e - 1))
    if (a * e) >= d:
        n2 = (a * e) - ((a * e) * (c / 100))
    else:
        n2 = a * e
    if n1 < n2:
        print(1)
        print(f"{n1:.02f}")
    elif n1 > n2:
        print(2)
        print(f"{n2:.02f}")
    else:
        print(2)
        print(f"{n2:.02f}")
main()
