def name_diamond(name):
    for i in range(len(name)+1):
        print(name[:i])
    for i in range(1,len(name)):
        print(i*' ',end='')
        print(name[i:])

name_diamond('MARTY')