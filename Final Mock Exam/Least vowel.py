"""Least vowel"""
def main():
    """Least vowel"""
    words = input()
    cleaned = ""
    for ch in words:
        if ('a' <= ch.lower() <= 'z') or ch.isspace():
            cleaned += ch
    words = cleaned.split()
     
    result = []
    for w in words:
        count = sum(ch in 'aeiou' for ch in w.lower())
        result.append([w, count])
    mins = min(c for _, c in result)
    print(' '.join(w for w, c in result if c == mins))
# main()

def main2():
    print(max(input()[::2]))
main2()
