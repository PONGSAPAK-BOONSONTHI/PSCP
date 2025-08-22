"""SumOfNumber"""
def main():
    """SumOfNumber"""
    is_sum = int(input())
    sum_num = 0
    num = 0
    while True:
        if sum_num == is_sum:
            break
        num = int(input())
        if num != -1:
            sum_num += num
        else:
            break
    print(sum_num)
main()
