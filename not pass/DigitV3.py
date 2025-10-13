"""DigitV3"""
def main():
    """DigitV3"""
    notation = {
        0 : "zero",
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "nine",
        10 : "ten",
        11 : "eleven",
        12 : "twelve",
        13 : "thirteen",
        14 : "fourteen",
        15 : "fifteen",
        16 : "sixteen",
        17 : "seventeen",
        18 : "eighteen",
        19 : "nineteen",
        20 : "twenty",
        30 : "thirty",
        40 : "forty",
        50 : "fifty",
        60 : "sixty",
        70 : "seventy",
        80 : "eighty",
        90 : "ninety",
        100 : "hundred",
        1000 : "thousand"
        }
    reverse_notation = dict(zip(notation.values(), notation.keys()))
    text_num = input().lower().split()
    # print(reverse_notation)
    total = 0
    current = 0
    for i in text_num:
        num = reverse_notation[i]
        if num == 100:
            current *= 100
        elif num == 1000:
            current *= 1000
            total += current
            current = 0
        else:
            current += num
    print(total + current)
main()
