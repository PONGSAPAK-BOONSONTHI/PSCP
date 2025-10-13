"""Remove Digits"""
def main():
    """Remove Digits"""
    num = input()
    while len(num) > 1:
        lists_nums = []
        len_num = len(num) - 1
        for i in range(len_num):
            new_num = num[:i] + num[i+2:]
            if new_num == "":
                new_num = "0"
            lists_nums.append(int(new_num))
            best_num = max(lists_nums)
        num = str(best_num)
    print(num)
main()
