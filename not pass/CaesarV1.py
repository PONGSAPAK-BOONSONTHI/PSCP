"""
Caesar V.1
"""
n = int(input())
txt = input()
ANS = ""
upper = False
for char in txt:
    ass = 0
    if char == " " or char == ".":
        ANS += char
        pass
    if char.isalpha():
        if char.isupper():
            upper = True
            char = char.lower()
        if ord(char) + n < 97:
            ass = ord(char) % 26
        else:
            ass = ord(char)
        t = chr(ass + n)
        if upper:
            t = t.upper()
            upper = False
        ANS += t
        pass
print(ANS)