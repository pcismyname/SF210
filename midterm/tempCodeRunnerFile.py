def top_bot(n):
    for i in range(n):
        for space in range(3*(n)):
            print(' ',end='')
        print('||')



def mid1(n):
    for i in range(n):
        for space in range(3*(n-i-1)):
            print(' ',end='')
        print('__/',end='')
        for point in range(i):
            print(':::',end='')
        print('||',end='')
        for point in range(i):
            print(':::',end='')
        print('\__',end='')
        print()


def mid2(n):
    print('|'+ 6*n*'"' + '|')
    for i in range(n):
        for space in range(i*2):
            print(' ',end='')
        print('\_',end='')
        for j in range(n*3-1-i*2):
            print('/\\',end='')
        print('_/',end='')
        print()



def draw(n):
    top_bot(n)
    mid1(n)
    mid2(n)
    top_bot(n)
