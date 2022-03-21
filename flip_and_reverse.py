def flip_and_reverse_lines():
    while True:
        file = input('Input file name? ')
        try:
            with open(file, 'r') as f:
                if f :
                    line = [i.strip('\n') for i in f.readlines()]
                    break
        except:
            print('Unable to open that file.  Try again.')
    for i in range (1,len(line),2):
        line[i], line[i-1] = line[i-1], line[i]
    for i in range (0,len(line)):
        if i%2 == 0:
            line[i] = line[i][::-1].upper()
        else:
            line[i] = line[i][::-1].lower()
    print()
    for i in line:
        print(i)


    


flip_and_reverse_lines()
