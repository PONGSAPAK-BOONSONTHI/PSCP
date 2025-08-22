"""Heron of Alexandria"""
import math
def main():
    """Heron of Alexandria"""
    a = float(input())
    b = float(input())
    c = float(input())
    s = (a + b + c) / 2
    result = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"{result:.3f}")
main()
