"""ProgressiveTax"""
def main():
    """ProgressiveTax"""
    sum_money = int(input())
    tax = 0
    if 4000000 < sum_money:
        tax += (sum_money - 4000000) * 0.35
    if 2000000 < sum_money:
        tax += (sum_money - 2000000) * 0.3 if sum_money < 4000000 else 2000000 * 0.3
    if 1000000 < sum_money:
        tax += (sum_money - 1000000) * 0.25 if sum_money < 2000000 else 1000000 * 0.25
    if 750000 < sum_money:
        tax += (sum_money - 750000) * 0.2 if sum_money < 1000000 else 250000 * 0.2
    if 500000 < sum_money:
        tax += (sum_money - 500000) * 0.15 if sum_money < 750000 else 250000 * 0.15
    if 300000 < sum_money:
        tax += (sum_money - 300000) * 0.1 if sum_money < 500000 else 200000 * 0.1
    if 150000 < sum_money:
        tax += (sum_money - 150000) * 0.05 if sum_money < 300000 else 150000 * 0.05
    print(int(tax))
main()
