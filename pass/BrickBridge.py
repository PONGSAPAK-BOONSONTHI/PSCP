"""BrickBridge"""
def main():
    """BrickBridge"""
    a = int(input())
    b = int(input())
    goal = int(input())
    maxs = min(b ,goal // 5)
    x = goal - (maxs * 5)
    if x <= a:
        print(x)
    else:
        print(-1)
main()
