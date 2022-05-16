def remove_even_length(lst):
    new = []
    for i in range(len(lst)):
        if len(lst[i]) %2 == 0:
            new.append(lst[i])
    for i in new:
        if i in lst:
            lst.remove(i)
    return lst


print(remove_even_length(["This", "is", "a", "test"]))
print(remove_even_length(['even', 'odd', 'ev', 'o'])
)