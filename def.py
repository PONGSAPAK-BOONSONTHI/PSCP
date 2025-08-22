def lowtext(text):
    """lower()"""
    result = ""
    for i in text:
        if "A" <= i <= "Z":
            result += chr(ord(i) + 32)
        else:
            result += i
    return result
def uptext(text):
    result = ""
    for i in text:
        if "a" <= i <= "z":
            result += chr(ord(i) - 32)
        else:
            result += i
    return result
def is_lowtext(text: str) -> bool:
    for i in text:
        if "A" <= i <= "Z":
            return False
    return True
def is_lowtext(text: str) -> bool:
    for i in text:
        if "a" <= i <= "z":
            return False
    return True
def replace_T(text, old: str, new: str) -> str:
    result = ""
    i = 0
    while i < len(text):
        if text[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += text[i]
            i += 1
    return result 
text = "132132s"
print(text)
print(replace_T(text, "13", "E"))