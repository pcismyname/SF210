def election():
    file = input('Input file? ')
    with open (file,'r') as f:
        line = [i.split() for i in f.readlines()]
        print(line)
        can1, can2 = 0, 0
        for i in line:
            if int(i[1]) > int(i[2]):
                can1 += int(i[3])
            elif int(i[1]) < int(i[2]):
                can2 += int(i[3])
        print(f'Candidate 1: {can1} votes')
        print(f'Candidate 2: {can2} votes')



election()
