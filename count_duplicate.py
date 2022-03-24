def count_duplicates(list):
    c = 0
    check = []
    for i in range (0,len(list)-1):
       for j in range(i+1,len(list)): 
           if list[i] == list[j] and list[i] not in check :
               c +=1
            
       check.append(list[i])
    print(c)
    return c


count_duplicates([1, 4, 2, 4, 7, 1, 1, 9, 2, 3, 4, 1])