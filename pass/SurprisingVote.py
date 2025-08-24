"""SurprisingVote"""
def main():
    """SurprisingVote"""
    a = float(input())
    b = float(input())
    vote2 =  a - b #29 - 10 = 19 
    # 20 - 8 = 12
    max_v = min(b, vote2) # 10, 19 = 10 
    # 8, 12 = 8
    vote = vote2 - max_v  # 19 - 10 
    # 12 - 8 = 4
    if b - 2 > vote: # 8 > 9 
    # 8 - 2 > 4
        print("Surprising")
    else:
        print("Not surprising")
main()
