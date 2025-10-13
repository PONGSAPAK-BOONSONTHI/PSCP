"""Duplicate I"""
def main():
    """Duplicate I"""
    m = int(input())
    n = int(input())
    list_m = set()
    list_n = set()
    for i in range(m + n):
        id_st = int(input())
        if i >= m:
            list_m.add(id_st)
        else:
            list_n.add(id_st)
    list_u = list(list_m & list_n)
    list_u.sort(reverse=True)
    if list_u:
        for i in list_u:
            print(i)
    else:
        print("Nope")
main()
