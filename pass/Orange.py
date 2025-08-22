"""Orange"""
def main():
    """Orange"""
    L = int(input())
    pay = int(input())
    on = 0
    for i in range(L + 1):
        on += i * i
    on = on - pay
    num = 0
    for i in range(L, 0, -1):
        if on <= 0:
            break
        on -=  i * i
        num += 1
    print(num)
main()
