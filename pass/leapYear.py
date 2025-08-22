"""leapYear"""
def main():
    """leapYear"""
    year = int(input())
    if year >= 100 and not year % 100:
        if not year % 400:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        if not year % 4:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
main()
