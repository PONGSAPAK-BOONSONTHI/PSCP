"""Elo"""
RA = int(input())
RB = int(input())
AC = input()
if AC == "A":
    pw = (RB - RA)/400
    result = 1 / (1 + 10**pw)
    print(f'{result:.2f}')
if AC == "B":
    pw = (RA - RB)/400
    result = 1 / (1 + 10**pw)
    print(f'{result:.2f}')
