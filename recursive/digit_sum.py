def digit_sum(num):
    if num < 0:
        num = abs(num)
        return -1 * (abs(num%10) + digit_sum(num//10))
    elif num == 0:
        return num
    else:
        return abs(num%10) + digit_sum(num//10)

