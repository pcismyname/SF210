table = [[0 for x in range(10)] for y in range(5)]


for i in range(len(table)):
    for j in range(len(table[0])):
        table[i][j] = i * j
        #print(table[i][j])
    
