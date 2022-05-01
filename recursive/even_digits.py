def even_digits(num):
    if num == 0:
        return num
    elif num < 0:
        return -1*even_digits(abs(num))
    if (num%10)%2 == 0:
        return num%10 + 10*even_digits(num//10)
    return even_digits(num//10)

print(even_digits(8342116))
print(even_digits(-8342116))