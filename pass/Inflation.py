"""Inflation"""
def main():
    """Inflation"""
    monny = float(input())
    y = int(input())
    monny = int(monny * 100)
    for _ in range(y):
        monny = monny + (monny * 381) // 10000
    print(f"{monny // 100}.{monny % 100:02d}")
main()
    