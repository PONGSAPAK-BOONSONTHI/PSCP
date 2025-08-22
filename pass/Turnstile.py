"""Turnstile"""
def main():
    """Turnstile"""
    ac_old = ""
    passs = 0
    while True:
        ac = input()
        if ac == "END":
            break
        if ac == "P" and ac_old == "C":
            ac_old = ""
            passs += 1
        elif ac == "C":
            ac_old = "C"
    print(passs)
main()
