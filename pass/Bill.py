"""Bill"""
def main():
    """"Bill"""
    price = int(input())
    bc = price * 0.1
    if bc <= 50:
        bc = 50
    else:
        if bc > 1000:
            bc = 1000
    result = (price + bc) + ((price + bc) * 0.07)
    print(f"{result:.2f}")
main()
