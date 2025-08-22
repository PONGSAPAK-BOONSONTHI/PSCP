"""OverlapCircle"""
import math
def main():
    """OverlapCircle"""
    x1 = int(input())
    y1 = int(input())
    r1 = int(input())
    x2 = int(input())
    y2 = int(input())
    r2 = int(input())
    m = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    m_cir = r1 + r2
    if m < m_cir:
        print("overlapping")
    elif m == m_cir:
        print("overlapping")
    else:
        print("no overlapping")
main()
