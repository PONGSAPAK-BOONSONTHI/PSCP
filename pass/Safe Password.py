"""Safe Password"""
def main():
    """Safe Password"""
    t = input()
    pw = int(input())
    tt = "H"
    pwt = 4567
    if t == tt and pw == pwt:
        print("safe unlocked")
    elif t == tt:
        print("safe locked - change digit")
    elif pw == pwt:
        print("safe locked - change char")
    else:
        print("safe locked")
main()
