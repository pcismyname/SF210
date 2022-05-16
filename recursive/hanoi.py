def hanoi(disk,start,end):
    if disk == 0:
        return 0
    else:
        print(f'move disk {disk} from peg {start} to peg {end}')
    else:
        if start == 1 and end == 2:
            temp = 3
        if start == 2 and end == 3:
            temp = 1
        if start == 1 and end == 3:
            temp =2
    hanoi(disk-1,start,temp)
    print(f'move disk {disk} from peg {start} to peg {end}')
    hanoi(disk-1,temp,end)



def move(start,stop):
    



hanoi(3,1,3)
