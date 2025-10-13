"""One For All"""
def main():
    """One For All"""
    num = int(input())
    result = ""
    for i in range(num):
        name = input()
        if i < num - 1:
            if not i % 2:
                result += name + ("*" * (i + 1))
            else:
                result += name + ("-" * (i + 1))
        else:
            result += f"{name}_{num}"
    print(result)
main()
