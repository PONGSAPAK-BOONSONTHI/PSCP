"""Diabete"""
import json
def main():
    """Diabete"""
    lists = json.loads(input())
    count_T = 0
    count_F = 0
    for i in lists:
        i = dict(i)
        name = i["name"]
        age = int(i["age"])
        sugar = i["sugar"]
        result = ""
        result = ""
        if 6 <= age <= 13 or 25 <= age:
            if sugar <= 16:
                result = "eat sugar within the limit"
                count_T += 1
            else:
                result = "eat too much sugar"
                count_F += 1
        elif 14 <= age < 25:
            if sugar <= 24:
                result = "eat sugar within the limit"
                count_T += 1
            else:
                result = "eat too much sugar"
                count_F += 1
        else:
            result = "error"
        print(f"{name} ({age}): {result}")
    print("")
    print(f"Exceed: {count_F}")
    print(f"Not Exceed: {count_T}")
main()
