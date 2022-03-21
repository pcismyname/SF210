def contaians(list1, list2):
    window = len(list2)
    if list1 == list2:
        return True
    for i in range(0,len(list1)-window):
        check = 0
        for j in range(0,window):
            if list1[i+j] == list2[j]:
                check += 1
        
        if check == window:
            return True
    return False