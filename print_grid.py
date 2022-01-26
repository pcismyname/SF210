def print_grid(m, n):

    for i in range(1, m+1):
        temp = i
        for j in range(1, n+1):
            if j == 1:
                if j == n:
                    print(i,end="")
                else:
                    print(i,end=", ")
            else :
                temp += m
                if j == n:
                    print(temp,end="")
                else :
                    print(temp,end=", ")
        print()

print_grid(4,1)