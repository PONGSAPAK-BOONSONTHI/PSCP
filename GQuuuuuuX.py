"""GQuuuuuuX"""
def main():
    """GQuuuuuuX"""
    text = input().upper()+" "
    i = 0
    UU = False
    num_U = 0
    num_Uold = 0
    while True:
        if i >= len(text):
            break
        if text[i:i+3] == "GQU":
            i += 3
            num_U = 1
            UU = True
            continue
        if UU and text[i] == "U":
            i += 1
            num_U += 1
            continue
        if UU and text[i] == "X":
            if num_Uold < num_U:
                num_Uold = num_U
            UU = False
            i += 1
            continue
        if UU:
            UU = False
            continue
        i += 1
    print(num_Uold if num_Uold else "None")
main()

"""GQuuuuuuX"""
def main2():
    """GQuuuuuuX"""
    text = input().upper()
    i = 0
    num_Uold = 0
    while i < len(text):
        if text[i:i+3] == "GQU":
            j = i + 3
            num_U = 1
            while j < len(text) and text[j] == "U":
                j += 1
                num_U += 1
            if j < len(text) and text[j] == "X":
                num_Uold = max(num_Uold, num_U)
            i += 1
        else:
            i += 1
    print(num_Uold if num_Uold else "None")
main2()