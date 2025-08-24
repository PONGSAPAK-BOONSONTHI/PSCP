"""Name of Card"""
def main():
    """Name of Card"""
    card = input().upper()\
        .replace("A", "Ace")\
        .replace("J", "Jack")\
        .replace("K", "King")\
        .replace("Q", "Queen")\
        .replace("S", " of Spades")\
        .replace("D", " of Diamonds")\
        .replace("H", " of Hearts")\
        .replace("C", " of Clubs")
    print(card)
main()
