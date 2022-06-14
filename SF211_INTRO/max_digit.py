def max_digit(number):
    number = str(number)
    lists = [int(x) for x in number]
    return max(lists)