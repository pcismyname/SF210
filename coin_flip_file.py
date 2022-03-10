def coin_file(file):
    with open(file,'r') as f:
        data = [i for i in f.read().split()]
        h ,t = 0, 0
        for i in data:
            if i.lower() in ['h','head','heads']:
                h += 1
            else :
                t += 1
        print(f'{h} heads ({int(h/(h+t)*100)}%)')
        if h/(h+t)*100 > 49:
            print('You win!')
        else :
            print('You lose!')
        
            


coin_file('file/coin.txt')