def ordinalDate(d, m, y):
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
    day = 0
    y -= 543
    if (y % 4 == 0 and y % 100 != 0) or y % 400 ==0 :   
        leap = True
    else :
        leap = False
    for i in range(m-1):
        if leap :
            month[1] = 29
        day += month[i]
    day += d
    return day

print(ordinalDate(31,12,256))