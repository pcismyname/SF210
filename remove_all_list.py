def remove_all(lst,alpha):
    while alpha in lst:
        lst.remove(alpha)
    return lst


print(remove_all(["a", "b", "c", "b", "b", "a", "b"], "b"))