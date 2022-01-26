def loop_mystery_exam(i,j):
    while i != 0 and j != 0:
        i = i // j
        j = (j - 1) // 2
        print(str(i) + " " + str(j) + " ",end ="")
    print(str(i))
    return i + j

a = loop_mystery_exam(1600, 40)
print(a)