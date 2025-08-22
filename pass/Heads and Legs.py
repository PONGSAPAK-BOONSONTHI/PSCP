"""Heads and Legs"""
def main():
    """Heads and Legs"""
    # x + y = a
    # y = a - x
    # 2x + 4y = b
    # 2x + 4(a - x) = b
    # 2x + 4a - 4x = b
    # -2x = b - 4a
    #  x = (4a - b) / 2
    #  x = 2 y = 3
    a = int(input())
    b = int(input())
    x = ((4*a) - b) / 2
    y = a - x
    if x < 0 or y < 0 or x % 1 or y % 1:
        print("Impossible")
    else:
        print(f"{y:.0f} {x:.0f}")
main()