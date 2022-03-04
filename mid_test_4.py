def firstDigit(s):
    for i in s:
        if i.isdigit():
            return int(i)
    return 0


print(firstDigit("By 30 years"))