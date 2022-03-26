c = 1
jagged = []
for i in range(5):
    col = []
    for j in range(i+1):
        col.append(c)
        c += 1
    jagged.append(col)

print(jagged)
        
    