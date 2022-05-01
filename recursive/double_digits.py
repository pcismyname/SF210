def double_digits(num):
    if num == 0:
        return num
    elif num >= 1:
        return int(str(double_digits(num//10)) + str(num%10)*2)
    else:
        num = abs(num)
        return int(str(double_digits(num//10)) + (str(num%10)*2))*(-1)


