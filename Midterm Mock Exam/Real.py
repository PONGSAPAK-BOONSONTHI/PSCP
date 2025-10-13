"""Real"""
def ck_LED(result ,LED):
    """ck_LED"""
    LED = LED[:-1]
    if LED == "1111110":
        result += "0"
    elif LED == "0110000":
        result += "1"
    elif LED == "1101101":
        result += "2"
    elif LED == "1111001":
        result += "3"
    elif LED == "0110011":
        result += "4"
    elif LED == "1011011":
        result += "5"
    elif LED == "1011111":
        result += "6"
    elif LED == "1110000":
        result += "7"
    elif LED == "1111111":
        result += "8"
    elif LED == "1111011":
        result += "9"
    return result
def main():
    """Real"""
    result = ""
    DP = 0
    for _ in range(3):
        LED = ""
        for _ in range(8):
            segment = input()
            LED += "1" if segment == "on" else "0"
        print(LED)
        result = ck_LED(result, LED)
        if LED[-1:] == "1":
            result += "."
            DP += 1
    print(f"{float(result):.02f}" if 0 <= DP <= 1 else "Error")
main()
