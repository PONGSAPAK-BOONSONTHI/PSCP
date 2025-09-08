"""Hamming"""
def main():
    """Hamming"""
    text1 = str(input())
    text2 = str(input())
    result = 0
    lentext = len(text1)
    for i in range(lentext):
        if text1[i] != text2[i]:
            result += 1
    print(result)
main()
