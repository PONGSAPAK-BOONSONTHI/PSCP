"""Coke"""
def main():
    """Coke"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    sum_money = 0
    num = 0
    for _ in range(d):
        if not b:
            sum_money += a
            continue
        if num == b:
            sum_money += c
            num = 0
        else:
            sum_money += a
        # print(i, sum_money)
        num += 1
    print(sum_money)
main()
