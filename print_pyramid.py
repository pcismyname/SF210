def print_pyramid():
    for i in range(1,7):
        for j in range(1,7-i+1):
            print(" ",end='')
        for j in range(1,2*i):
            print('*',end='')
        print()

print_pyramid()