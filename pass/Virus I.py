"""Virus I"""
def main():
    """Virus I"""
    virus = input()
    num_virus = 0
    for i in virus:
        if i == "o":
            num_virus += 1
    print(num_virus)
main()
