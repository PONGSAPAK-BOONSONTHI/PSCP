"""IT Business"""
def sp(ac_all): #split
    """split"""
    ac = ""
    money = ""
    ac_t = False
    for i in ac_all:
        if i == " " and not ac_t:
            ac_t = True
            continue
        if ac_t:
            money += i
        else:
            ac += i
    money = float(money)
    return ac, money
def main():
    """IT Business"""
    money_ac = float(input())
    money_me = float(input())
    error = 0
    while True:
        if error >= 3:
            break
        ac_all = input()
        if ac_all == "end":
            break
        ac, money = sp(ac_all)
        if ac == "D" :
            if money_me >= money:
                money_ac += money
                money_me -= money
                error = 0
            else:
                error += 1
        elif ac == "W":
            if money_ac >= money:
                money_me += money
                money_ac -= money
                error = 0
            else:
                error += 1
        else:
            error += 1
    print(f"{money_ac:.2f}")
    print(f"{money_me:.2f}")
main()
