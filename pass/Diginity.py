"""Diginity"""
def main():
    """Diginity"""
    while True:
        num = input()
        if num == "0":
            break
        while len(str(num)) > 1:
            now_num = 0
            for i in num:
                now_num += int(i)
            num = str(now_num)
        print(num)
main()
