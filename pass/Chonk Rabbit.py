"""Chonk Rabbit"""
def main():
    """Chonk Rabbit"""
    num_list = int(input())
    dict_rab = {}
    conut = 0
    for _ in range(num_list):
        name_rab, w_rab = input().split()
        w_rab = int(w_rab)
        dict_rab[name_rab] = w_rab
        if w_rab > 15:
            conut += 1
    print(conut)
    name, w = zip(*dict_rab.items())
    print(name[w.index(max(w))], max(w))
main()
