"""EuclideanDistance2D"""
import math
def main():
    """EuclideanDistance2D"""
    q1 = float(input())
    q2 = float(input())
    p1 = float(input())
    p2 = float(input())
    result = math.sqrt((q1 - p1)**2 + (q2 - p2)**2)
    print(result)
main()
