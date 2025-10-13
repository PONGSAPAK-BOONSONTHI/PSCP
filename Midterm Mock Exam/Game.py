"""Game"""
def main():
    """Game"""
    A = int(input()) % 3
    B = int(input()) % 3
    print("Error" if A > B or A < B else A)
main()
