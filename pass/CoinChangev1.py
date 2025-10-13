"""CoinChangev1"""
def main():
    """CoinChangev1"""
    money = int(input())
    coin = 0
    while money:
        if money >= 25:
            money = money - 25
        elif money >= 10:
            money = money - 10
        elif money >= 5:
            money = money - 5
        elif money >= 1:
            money = money - 1
        coin += 1
    print(coin)
main()
