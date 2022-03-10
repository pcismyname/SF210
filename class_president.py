def class_presidents(file):
    with open(file,'r') as f:
        data = [i for i in f.read().split()]
        fmax = 0
        smax = 0
        sname =''
        fname =''
        for i in range(1, len(data), 3):
            if data[i] == 's':
                if smax < int(data[i+1]):
                    sname = data[i-1]
                    smax =  int(data[i+1])
            else :
                if fmax < int(data[i+1]):
                    fname = data[i-1]
                    fmax =  int(data[i+1])

        print(f'Sophomore Class President: {sname} ({smax} votes)')
        print(f'Junior Class President: {fname} ({fmax} votes)')


class_presidents('file/class.txt')        
        