"""TicTacToe"""
def main():
    """TicTacToe"""
    rs = ""
    for _ in range(3):
        line = input()
        rs += line
    result = ""
    if rs[0] == rs[1] == rs[2] and rs[0] != "-":
        result = f"{rs[0]} WIN"
    if rs[3] == rs[4] == rs[5] and rs[3] != "-":
        result = f"{rs[3]} WIN"
    if rs[6] == rs[7] == rs[8] and rs[6] != "-":
        result = f"{rs[6]} WIN"

    if rs[0] == rs[3] == rs[6] and rs[0] != "-":
        result = f"{rs[0]} WIN"
    if rs[1] == rs[4] == rs[7] and rs[1] != "-":
        result = f"{rs[1]} WIN"
    if rs[2] == rs[5] == rs[8] and rs[2] != "-":
        result = f"{rs[2]} WIN"

    if rs[0] == rs[4] == rs[8] and rs[0] != "-":
        result = f"{rs[0]} WIN"
    if rs[2] == rs[4] == rs[6] and rs[2] != "-":
        result = f"{rs[2]} WIN"
    print(result if result else "DRAW")
main()
