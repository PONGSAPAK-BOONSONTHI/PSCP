"""RuleofThree"""
def main():
    """RuleofThree"""
    num = int(input())
    max_price_k = float('-inf')
    put_price = 0
    put_k = 0
    for _ in range(num):
        price = float(input())
        k = float(input())
        price_k = k / price
        if (max_price_k < price_k) or (price_k == max_price_k and price < put_price):
            put_price = price
            put_k = k
            max_price_k = price_k
    print(f"{put_price:.2f} {put_k:.2f}")
main()
