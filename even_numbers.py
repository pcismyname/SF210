def even_numbers(file):
    with open(file,'r') as f:
        num = [int(i) for i in f.read().split()]
        sum, c = 0, 0
        for i in num:
            sum += i
            if i%2 == 0:
                c += 1

        print(f'{len(num)} numbers, sum = {sum}')
        print(f'{c} evens ({c/len(num)*100:.1f}%)')

even_numbers('file/even.txt')