"""Century"""
def main():
    """Century"""
    num = int(input())
    for _ in range(num):
        name_year, num_year = input().split()
        num_year = int(num_year)
        if name_year in ("B.E.", "พ.ศ."):
            num_year -= 543
        elif name_year in ("A.D.", "ค.ศ."):
            pass
        else:
            print("ERROR")
            continue
        if num_year <= 0:
            print("ERROR")
            continue
        if not num_year % 100:
            re = num_year // 100
        else:
            re = num_year // 100 + 1
        print(re)
main()
