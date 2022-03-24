def has_mirror_twice(a1,a2):
    check = 0
    twice = 0
    if len(a2) == 1:
        flag = 1
    else:
        flag = 0
    for i in  range(len(a1)-len(a2)+flag):
        check = 0
        for j in range(len(a2)):
            if a2[len(a2)-j-1] == a1[i+j]:
                check +=1
        if check == len(a2):
            twice += 1
    if twice == 2:
        return True
    else:
        return False

a1 = [6, 1, 2, 1, 3, 1, 3, 2, 1, 5]
a2 = [1, 2]
print(has_mirror_twice(a1, a2))
print(has_mirror_twice([0, 0], [0]))