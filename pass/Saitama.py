"""Saitama"""
import math
def main():
    """Saitama"""
    do1 = int(input())
    do2 = int(input())
    do3 = int(input())
    do4 = int(input())
    ac1 = int(input())
    ac2 = int(input())
    ac3 = int(input())
    ac4 = int(input())
    doac1 = math.ceil(do1 / ac1)
    doac2 = math.ceil(do2 / ac2)
    doac3 = math.ceil(do3 / ac4)
    doac4 = math.ceil(do4 / ac3)
    mas = doac1
    if doac2 > mas:
        mas = doac2
    if doac3 > mas:
        mas = doac3
    if doac4 > mas:
        mas = doac4
    print(mas)
main()
