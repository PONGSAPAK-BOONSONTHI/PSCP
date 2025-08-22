"""999 Pairing"""
def main():
    """999 Pairing"""
    num = int(input())
    pw1 = input()
    pw2 = input()
    er = 0
    for i in range(num):
        if int(pw1[i]) + int(pw2[i]) != 9:
            er += 1
    if not er:
        print("YES")
    else:
        print(f"NO {er}")
main()
