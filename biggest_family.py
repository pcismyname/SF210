import collections

def biggest_family(file):
    with open (file,'r') as f:
        data  = [i.strip('\n') for i in f.readlines()]
        names = [i.split() for i in data]
        family = {i[1] : [] for i in names}
        max = 0
        for key in family:
            for i in names:
                if key == i[1]:
                    family[key].append(i[0])
            num = len(family[key])
            family[key].sort()
            if num > max:
                max = num
        od = collections.OrderedDict(sorted(family.items()))
        for i, j in od.items():
            if len(j) == max:
                print(f'{i} family: ',end='')
                for k in j:
                    print(f'{k} ',end='')
                print()

        #print(od)           
        #print(family)
        #print(max)



biggest_family('file/biggest_family.txt')