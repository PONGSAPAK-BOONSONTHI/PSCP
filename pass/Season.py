"""Season"""
def main():
    """Season"""
    month = int(input())
    day = int(input())
    season = 0
    if month <= 3:
        season = 0
    elif month <= 6:
        season = 1
    elif month <= 9:
        season = 2
    elif month <= 12:
        season = 3
    if not month % 3 and day >= 21:
        season = (season + 1) % 4
    seasons = ["winter", "spring", "summer", "fall"]
    print(seasons[season])
main()
