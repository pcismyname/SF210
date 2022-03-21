def flip_coins(file):
    with open (file, 'r') as f:
        line = [i.strip('\n').lower().split() for i in f.readlines()]
        #print(line)

        for coin in line:
            h, t = 0, 0
            for side in coin:
                if side == 'h':
                    h += 1
                else:
                    t += 1
            print(f'{h} heads ({int(h/(h+t)*100)}%)')
            if h > t :
                print('There were more heads!')
            print()



print(flip_coins('file\\flip.txt'))
