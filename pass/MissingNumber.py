"""MissingNumber"""
def main():
    """MissingNumber"""
    num = int(input())
    check_list_num = {i + 1 for i in range(num)}
    list_num = []
    while True:
        n = int(input())
        if not n:
            break
        list_num.append(n)
    list_num = set(list_num)
    result = check_list_num - list_num
    result = sorted(result)
    for i in result:
        print(i)
main()
