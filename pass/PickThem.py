"""PickThem"""
import json
def main():
    """PickThem"""
    list_num = input()
    list_num = json.loads(list_num)
    list_even = [i for i in list_num if not i % 2]
    if list_even:
        for i in list_even:
            print(i)
    else:
        print("Nope")
main()
