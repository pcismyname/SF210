def mystery(lis):
    for i in range(len(lis) - 1, 0,-1):
        if lis[i] < lis[i -1]:
            element = lis[i]
            lis.pop(i)
            lis.insert(0,element)
    print(lis)

mystery([2, 6, 1, 8])
mystery([30, 20, 10, 60, 50, 40])
mystery([-4, 16, 9, 1, 64, 25, 36, 4, 49])