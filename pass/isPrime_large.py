"""isPrime_large"""
def main():
    """isPrime_large"""
    num = int(input())
    result = num >= 2
    for i in range(2, int(num**0.5) + 1):
        if not num % i:
            result = False
    print("YES" if result else "NO")
main()
