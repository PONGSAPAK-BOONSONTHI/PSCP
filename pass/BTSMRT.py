"""BTSMRT"""
def main():
    """BTSMRT"""
    day = input()
    age = float(input())
    h = float(input())
    if day == "Children Day" and age < 14 and h <= 140:
        print("FREE")
    elif age < 14 and h < 90:
        print("FREE")
    elif day == "Senior Day" and age >= 60:
        print("FREE")
    else:
        print("PAY")
main()
