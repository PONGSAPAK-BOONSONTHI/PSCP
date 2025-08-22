"""FOR!F-Ball"""
def main():
    """FOR!F-Ball"""
    ac = input()
    ps = 1
    for i in ac:
        if i == "A":
            ps = 1 if ps == 2 else 2 if ps == 1 else ps
        if i == "B":
            ps = 2 if ps == 3 else 3 if ps == 2 else ps
        if i == "C":
            ps = 1 if ps == 3 else 3 if ps == 1 else ps
    print(ps)
main()
