def max_length(set_str):
    maxi = 0
    for i in set_str:
        num = len(i)
        if num > maxi:
            maxi = num
    return maxi