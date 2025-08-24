"""GQuuuuuuX"""
def main():
    """GQuuuuuuX"""
    text = input().upper()
    i = 0
    num_U = 0
    num_Uold = 0
    while i < len(text):
        if text[i:i+3] == "GQU":
            j = i + 3
            num_U += 1
            while j < len(text) and text[j] == "U":
                j += 1
                num_U += 1
            if j < len(text) and text[j] == "X":
                if num_Uold < num_U:
                    num_Uold = num_U
            i += 1
        else:
            i += 1
    print(num_Uold if num_Uold else "None")
main()
