def is_stack_sorted(stack):
    store = []
    flag = True
    num = len(stack)
    temp = stack.pop()
    store.append(temp)
    while stack != []:
        prev = temp
        temp = stack.pop()
        if prev >  temp:
            flag = False
        store.append(temp)
    while store != []:
        stack = store.pop()

    if flag:
        return flag
    else :
        return flag

print(is_stack_sorted([20, 20, 17, 11, 8, 8, 3, 2]))
print(is_stack_sorted([18, 12, 15, 6, 1]
))

