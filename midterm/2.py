def sumAllDigits(s):
    sum = 0
    for i in s:
        if i.isdigit():
            sum += int(i)
    return sum

print(sumAllDigits("By 25 Feb 2022"))

