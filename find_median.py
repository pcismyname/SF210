def find_median(list):
    list.sort()
    if len(list)%2 == 0 :
        return (list[len(list)/2] + list[(len(list)/2)+1])/2
    else :
        return list[int(len(list)/2)]


list = [5, 2, 4, 17, 55, 4, 3, 26, 18, 2, 17]
print(find_median(list))