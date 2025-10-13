"""Post Office"""
def defnn(nn):
    """defnn"""
    price_n = 0
    if 0 <= nn <= 10:
        price_n += 16
    elif 10 < nn <= 20:
        price_n += 18
    elif 20 < nn <= 100:
        price_n += 23
    elif 100 < nn <= 250:
        price_n += 28
    elif 250 < nn <= 500:
        price_n += 33
    elif 500 < nn <= 1000:
        price_n += 48
    elif 1000 < nn <= 2000:
        price_n += 68
    return price_n
    
def main():
    """Post Office"""
    n = int(input())
    m = int(input())
    price_m = 0
    price_n = 0
    price_mm = 0
    price_nn = 0
    for i in range(n + m):
        if i > n - 1:
            mm = float(input())
            if 0 <= mm <= 500:
                price_m += 45
            elif 500 < mm <= 1000:
                price_m += 55
            elif 1000 < mm <= 2000:
                price_m += 70
            price_mm = price_m + (m * 15)
        else:
            nn = float(input())
            price_n += defnn(nn)
            price_nn = price_n + (n * 13)
    print(price_mm + price_nn)
main()
