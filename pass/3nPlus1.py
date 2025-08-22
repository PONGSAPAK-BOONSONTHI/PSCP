"""3nPlus1"""
def main():
    """3nPlus1"""
    num_list = []
    while True:
        n = int(input())
        if not n:
            break
        num_list.append(n)
    for i in num_list:
        result = 0
        while True:
            if i == 1:
                result += 1
                break
            if not i % 2:
                i = i / 2
                result += 1
            else:
                i = (i * 3) + 1
                result += 1
        print(result)
main()
