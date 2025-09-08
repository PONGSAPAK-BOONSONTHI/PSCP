"""Key"""
def main():
    """Key"""
    key_id = input()
    sum_id = sum(int(i) for i in key_id) + (int(key_id[10:13]) * 10)
    if sum_id < 1000:
        sum_id += 1000
    print(f"{sum_id%10000:04d}")
main()
