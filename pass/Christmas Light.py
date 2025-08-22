"""Christmas Light"""
def main():
    """"Christmas Light"""
    col = input()
    num = int(input())
    result = ""
    set_col = []
    if col == "R":
        set_col = ["Red ", "Green ", "Blue "]
    elif col == "G":
        set_col = ["Green ", "Blue ", "Red "]
    elif col == "B":
        set_col = ["Blue ", "Red ", "Green "]
    for i in range(num):
        result += set_col[i % 3]
    print(result)
main()
