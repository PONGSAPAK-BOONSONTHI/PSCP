"""Align"""
import math
def main():
    """Align"""
    size = int(input())
    pos = input()
    text = input()
    gap = size - len(text)
    if pos == "left":
        print(text + " " * gap)
    elif pos == "center":
        gap = gap / 2
        print(" " * math.ceil(gap) + text + " " * math.floor(gap))
    elif pos == "right":
        print(" " * gap + text)
main()
