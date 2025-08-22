"""GCD_2"""
def main():
    """GCD_2"""
    a = int(input())
    b = int(input())
    while b:
        a, b = b, a % b
    print(a)
main()
