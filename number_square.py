def number_square(a,b):
    for i in range(a,b+1):
        for j in range(i,b+1):
            print(j,end='')
        for j in range(a,i):
            print(j,end='')
        print()

number_square(1,5)
