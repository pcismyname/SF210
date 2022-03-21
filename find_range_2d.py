def find_range_2d(list):
    data = []
    for i in list:
        for j in i:
            data.append(j)
    return max(data) - min(data) +1

    

print(find_range_2d([[8, 3], [5, 7], [2, 4]]))