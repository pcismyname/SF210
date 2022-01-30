def even_sum_max():
    n = int(input("how many integers? "))
    sum = 0
    max = -1
    while n :
        num = int(input("next integer? "))
        if num % 2 == 0:
            if num > max :
                max = num
            sum += num
        n-=1
    print(f'even sum = {sum}')
    print(f'even max = {max}')

even_sum_max()