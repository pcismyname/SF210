def countEvenDigits(n):
    if n < 0:
        n *= -1
    n = str(n)
    count = 0
    for i in n:
        if int(i) % 2 == 0:
            count += 1
    return count

print(countEvenDigits(-1123456))



