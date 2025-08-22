"""Temperature"""
def kv(x):
    """Kv"""
    re = x + 273.15
    print(f"{re:.2f}")
def fh(x):
    """Fh"""
    re = x * (9/5) + 32
    print(f"{re:.2f}")
def rk(x):
    """Rk"""
    re = (x + 273.15) * (9/5)
    print(f"{re:.2f}")
def tpt(a2 ,tem):
    """Tpt"""
    if a2 == "C":
        print(f"{tem:.2f}")
    elif a2 == "K":
        kv(tem)
    elif a2 == "F":
        fh(tem)
    elif a2 == "R":
        rk(tem)
def main():
    """Temperature"""
    tem = float(input())
    a1 = input()
    a2 = input()
    if a1 == "C":
        tpt(a2, tem)
    elif a1 == "K":
        tem = tem - 273.15
        tpt(a2, tem)
    elif a1 == "F":
        tem = (tem * (5/9)) - (160 / 9)
        tpt(a2, tem)
    elif a1 == "R":
        tem = (tem * (5/9)) - 273.15
        tpt(a2, tem)
main()
