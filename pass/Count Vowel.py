"""Count Vowel"""
def main():
    """Count Vowel"""
    num = int(input())
    result = 0
    for _ in range(num):
        let = input().lower()
        if let in ["a", "e", "i", "o", "u"]:
            result += 1
    print(result)
main()
