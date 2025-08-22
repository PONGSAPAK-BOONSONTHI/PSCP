"""PickThemAgain"""
def main():
    """PickThemAgain"""
    set_num = input().split()
    Nope = False
    for i in reversed(set_num):
        i = int(i)
        if (not i % 3 or not i % 5) and i != 1:
            print(i)
            Nope = True
    if not Nope:
        print("Nope")
main()
