"""Pig"""
def main():
    """Pig"""
    num = int(input())
    lists = input().split(" ")
    N = 0
    W = 0
    num_list = []
    while N < num:
        ac = max(int(lists[W]), int(lists[W + 1]))
        num_list.append(str(ac))
        W += 2
        N += 1
    if num > 1:
        result = " + ".join(num_list)
        print(result, "=", sum(int(i) for i in num_list))
    else:
        print(num_list[0])
main()
