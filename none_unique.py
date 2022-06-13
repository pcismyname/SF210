items= [1, 1, 2, 2, 3, 3]
border = 2
flag = 0
new = []
for i in items:
    if i == border:
        flag = 1
        new.append(i)
        continue
    if flag == 1:
        new.append(i)
print(new)