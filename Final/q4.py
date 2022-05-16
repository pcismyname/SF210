def split_set(data):
    first = set()
    second = set()
    for i in data:
        if i < 0:
            first.add(i)
        else:
            second.add(i)
    output =(first,second)
    return output


print(split_set({1,2,3}))