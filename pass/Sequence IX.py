"""Sequence Ix"""
def main():
    """Sequence Ix"""
    num = int(input())
    wp = num
    for i in range(num):
        n_out = 0
        result = 0
        row = num + i
        for _ in range(row):
            n_out += 1
            if n_out > num:
                result -= 1
                if _ == row - 1:
                    print(f"{result:02}")
                else:
                    print(f"{result:02}", end=" ")
            elif wp <= n_out <= num:
                result += 1
                if _ == row - 1:
                    print(f"{result:02}")
                else:
                    print(f"{result:02}", end=" ")
            else:
                if _ == row - 1:
                    print(" ")
                else:
                    print("  ", end=" ")
        wp -= 1
main()
