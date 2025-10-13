"""Ascending Sort"""
def main():
    """Ascending Sort"""
    count = int(input())
    list_num = []
    for _ in range(count):
        num = int(input())
        list_num.append(num)
    list_num.sort()
    print(*list_num, sep="\n")
main()
