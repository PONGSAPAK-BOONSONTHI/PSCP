"""Inflation"""
import math
def main():
    """Inflation"""
    monny = float(input())
    y = int(input())
    while y > 0:
        monny = math.floor(monny * 1.0381 * 1000000) / 1000000
        y -= 1
    print(f"{monny:.2f}")
main()
