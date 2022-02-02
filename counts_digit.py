def count_digits(num):
    num = abs(num)
    c = 0
    while num > 0 :
        num //=10
        c += 1
    return c

print(count_digits(-72))
