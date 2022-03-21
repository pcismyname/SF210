def count_coins(file):
    with open (file,'r') as f :
        data = [i for i in f.read().split()]
        cent = 0
        for i in range(0,len(data)) :
            if data[i].lower() == 'pennies':
                cent += int(data[i-1])
            elif data[i].lower() == 'nickels':
                cent += int(data[i-1]) * 5
            elif data[i].lower() == 'dimes':
                cent += int(data[i-1]) * 10
            elif data[i].lower() == 'quarters':
                cent += int(data[i-1]) * 25

        print(f'${cent/100}')


count_coins('file\count_coin.txt')