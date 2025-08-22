"""Sequence VIII"""
def main():
    """Sequence VIII"""
    num = int(input())
    wp = num
    for _ in range(num):
        n_out = 0
        result = 0
        for _ in range(num):
            n_out += 1
            if n_out >= wp:
                result += 1
                if _ == num - 1:
                    print(f"{result:02}")
                else:
                    print(f"{result:02}", end=" ")
            else:
                if _ == num - 1:
                    print("  ")
                else:
                    print("  ", end=" ")
        wp -= 1
main()
