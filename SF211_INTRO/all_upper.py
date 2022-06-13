from distutils import text_file


def is_all_upper(text: str) -> bool:
    #text = text.split()
    flag = 1
    for i in text:
        if i.islower():
            flag = 0
    return bool(flag)

print(is_all_upper('ALL UPPER') == True)
print(is_all_upper('all lower') == False)
print(is_all_upper('mixed UPPER and lower') == False)
print(is_all_upper('') == True)
print(is_all_upper('444') == True)
print(is_all_upper('55 55 5') == True)