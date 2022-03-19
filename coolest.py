

def coolest(file):
    with open(file,'r') as f:
        data = [i for i in f.read().split()]
        name = []
        for i in range (0,len(data)) :
            if i%2 != 0 and  data[i] not in name:
                name.append(data[i])
        print(name)
        follower = []
        for i in range (0,len(data)) :
            if i%2 == 0 and  data[i] not in follower:
                follower.append(data[i])

        right = []
        for i in range (0,len(data)) :
            if i%2 != 0 and  data[i]:
                right.append(data[i])
        print(right)
        count = []
        for i in name:
            c = 0
            for j in  range (0,len(data)):
                 if j%2 != 0 :
                    if i == data[j]:
                        c += 1
            count.append(c)
        print(count)

        score = []
        for i in range(0,len(name)):
            for j in range(0,len(follower)):
                
                


                        
        


coolest('file/twitter.txt')