import random
def coin_flip(k,side):
    if k < 0:
        print('ERROR!')
        return
    if side != 'H' and side != 'T':
        print('ERROR!')
        return 
    c = 0
    if k == 0:
        print(f'You got {side} {k} times in a row!')
        return
    while(True):
        coin =  random.choice(['H', 'T'])
        print(coin,end=" ")
        if coin == side:
            c += 1
        else :
            c = 0
        if k == c:
            break
    print()
    print(f'You got {side} {k} times in a row!')

coin_flip(4,'T')
        

    