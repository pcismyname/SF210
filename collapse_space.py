def collapse_spaces(file):
    with open(file,'r') as f:
        for i in f.readlines():
            i = i.split()
            for j in i:
                print(j,end=' ')
            print()



collapse_spaces('file\collapese.txt')