def print_design():
    l,r,num = 6,6,1
    for i in range(1,6):
        for j in range(1,12):
            if j >= l and j <= r:
                print(num,end='')
            else:
                print('-',end='')
        l -= 1
        r += 1
        num += 2
        print()

print_design()