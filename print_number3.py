def print_number3():
    for i in range(1,6):
        for j in range(1,6):
            if 6 - i == j:
                print(i,end='')
            else :
                print('.',end='')
        print() 


print_number3()