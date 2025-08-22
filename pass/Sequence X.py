"""Sequence X"""
def main():
    """Sequence X"""
    num = int(input())
    wp = num
    for i in range(num):
        result = 0
        for j in range(num + i):
            if j >= num:
                result -= 1
                print(f"{result:02}", end=" \n"[j == num + i - 1])
            elif wp <= j + 1:
                result += 1
                print(f"{result:02}", end=" \n"[j == num + i - 1])
            else:
                print("  ", end=" \n"[j == num + i - 1])
        wp -= 1
    wp = 2
    for i in range(num - 2, -1, -1):
        result = 0
        for j in range(num + i):
            if j >= num:
                result -= 1
                print(f"{result:02}", end=" \n"[j == num + i - 1])
            elif wp <= j + 1:
                result += 1
                print(f"{result:02}", end=" \n"[j == num + i - 1])
            else:
                print("  ", end=" \n"[j == num + i - 1])
        wp += 1
main()
