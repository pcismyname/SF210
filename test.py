def print_average():
    count = 0
    sum = 0
    num = int(input("Type a number: "))
    count += 1
    sum += num
    if num < 0:
        return
    while(True):
        num = int(input("Type a number: "))
        if(num < 0):
            break
        sum += num
        count += 1
    print(f'Average was {sum/count}')


print_average()
