"""GCD_N"""
import math
def main():
    """GCD_N"""
    ac_num = int(input())
    gcd_old = 0
    for _ in range(ac_num):
        num = int(input())
        if gcd_old:
            gcd_old = math.gcd(gcd_old, num)
        else:
            gcd_old = num
    print(gcd_old)
main()
