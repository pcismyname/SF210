def print_factors(num):
    for i in range(1,num):
        if num%i == 0:
            print(i,end = " and ")

    print(num)

print_factors(24)