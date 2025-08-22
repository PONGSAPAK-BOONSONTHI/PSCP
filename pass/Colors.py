"""Colors"""
def main():
    """Colors"""
    c1 = input()
    c2 = input()
    match c1:
        case "Red":
            if c2 == "Yellow":
                print("Orange")
            elif c2 == "Blue":
                print("Violet")
            elif c1 == c2:
                print("Red")
            else:
                print("Error")
        case "Yellow":
            if c2 == "Red":
                print("Orange")
            elif c2 == "Blue":
                print("Green")
            elif c1 == c2:
                print("Yellow")
            else:
                print("Error")
        case "Blue":
            if c2 == "Red":
                print("Violet")
            elif c2 == "Yellow":
                print("Green")
            elif c1 == c2:
                print("Blue")
            else:
                print("Error")
        case _ :
            print("Error")
main()
