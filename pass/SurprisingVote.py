"""SurprisingVote"""
def main():
    """SurprisingVote"""
    a = float(input())
    b = float(input())
    vote2 =  a - b
    max_v = min(b, vote2)
    vote = vote2 - max_v
    if b - 2 > vote:
        print("Surprising")
    else:
        print("Not surprising")
main()
