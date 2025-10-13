"""Median"""
def main():
    """Median"""
    num = input().split(", ")
    num = sorted([float(x) for x in num])
    n = len(num)
    if not n % 2:
        ps1 = n // 2 - 1
        ps2 = n // 2
        result = (num[ps1] + num[ps2]) / 2
    else:
        ps = n // 2
        result = num[ps]
    print(f"{result:.2f}")
main()
