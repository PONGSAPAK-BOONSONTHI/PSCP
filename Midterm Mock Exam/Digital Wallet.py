"""Digital Wallet"""
def main():
    """Digital Wallet"""
    name = input()
    th = input()
    home = input()
    age = float(input())
    y = float(input())
    mn = float(input())
    DW = False
    if th == "Yes" or th == "True":
        if home == "Yes" or home == "True":
            if age >= 16:
                if y <= 840000:
                    if mn <= 500000:
                        DW = True
    if DW:
        print(f"Congratulations! {name} is qualified to receive a digital \
wallet amount of 10,000 baht, sponsored by all taxpayers in Thailand.")
    else:
        print(f"Unfortunately, {name} is not qualified.")
main()
