"""PhoneNumber"""
def main():
    """PhoneNumber"""
    phone = input()
    if_phone = input()
    f_phone = ""
    if if_phone == "International":
        if len(phone) >= 10:
            f_phone = phone[1]
        print(f"+66{f_phone}", phone[-8:-4], phone[-4:])
    if if_phone == "Domestic":
        if len(phone) >= 10:
            f_phone = phone[1]
        print(f"0{f_phone}", phone[-8:-4], phone[-4:])
main()
