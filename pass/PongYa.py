"""PongYa"""
def main():
    """PongYa"""
    n = int(input())
    say = ""
    for i in range(1, n + 1):
        if not i % 3 or i % 10 == 3:
            say = "PONG"
        else:
            say = i
    print(say)
main()
