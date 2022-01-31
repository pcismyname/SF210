def count_quarters(num):
    num %= 100
    return num//25

print(count_quarters(1278))