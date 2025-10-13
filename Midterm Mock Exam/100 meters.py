"""100 meters"""
def ck(n, n11, n22, n33, n44, n55, n66, n77, n88):
    """100 meters"""
    if n == n11: n = 1
    if n == n22: n = 2
    if n == n33: n = 3
    if n == n44: n = 4
    if n == n55: n = 5
    if n == n66: n = 6
    if n == n77: n = 7
    if n == n88: n = 8
    return n
def main():
    """"100 meters"""
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    n4 = float(input())
    n5 = float(input())
    n6 = float(input())
    n7 = float(input())
    n8 = float(input())
    n11, n22, n33, n44, n55, n66, n77, n88 = n1 ,n2 ,n3 ,n4 ,n5, n6, n7, n8
    for _ in range(8):
        if n1 > n2: n1, n2 = n2, n1
        if n2 > n3: n2, n3 = n3, n2
        if n3 > n4: n3, n4 = n4, n3
        if n4 > n5: n4, n5 = n5, n4
        if n5 > n6: n5, n6 = n6, n5
        if n6 > n7: n6, n7 = n7, n6
        if n7 > n8: n7, n8 = n8, n7
    # print(n1 ,n2 ,n3 ,n4 ,n5, n6, n7, n8)
    n1 = ck(n1, n11, n22, n33, n44, n55, n66, n77, n88)
    n2 = ck(n2, n11, n22, n33, n44, n55, n66, n77, n88)
    n3 = ck(n3, n11, n22, n33, n44, n55, n66, n77, n88)
    print(n1, n2, n3)
main()
