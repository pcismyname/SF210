def count_unique(list):
    c = 0
    check = []
    if len(list) == 0:
        return 0
    for i in range (0,len(list)-1):
        for j in range(i+1,len(list)): 
            if list[i] != list[j] and list[i] not in check:
                c +=1
                check.append(list[i])
             
        check.append(list[i])
    if c == 0:
        return 1     
    #print(c)
    return c   


count_unique([7, 7, 2, 2, 1, 2, 2, 7])