import random

def flip_coin_three_heads():
    count = 0
    while count < 3:
        coin =  random.choice([True, False])
        if coin:
            count += 1
            print("H",end = ' ')
        else:
            count = 0
            print("T",end=' ')
    print() 
    print("Three heads in a row!")

flip_coin_three_heads()