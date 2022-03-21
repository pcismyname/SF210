def double_list(list):
    list2 = list.copy()
    max = len(list) * 2
    c = 0
    for i in range(0,max,2):
        list.insert(i,list2[c])
        c += 1
    return list

print(double_list(["how", "are", "you?"]))
print(double_list(['I', 'am', 'great,', 'thanks!']))