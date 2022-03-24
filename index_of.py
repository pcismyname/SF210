def index_of(list, num):
    for i in range(len(list)):
        if list[i] == num:
            return i
    return -1