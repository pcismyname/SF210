def convert_to_alt_caps(word):
    new = ''
    char = 0
    for i in range(0,len(word)):
        if word[i] == ' ':
            new += ' '
            continue
        char += 1
        if char % 2 != 0:
            x = word[i].lower()
        else :
            x = word[i].upper()
        new += x
    return new

print(convert_to_alt_caps('this  is   a     test'))
