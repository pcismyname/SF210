import math 
def star(n) :
    n = int(n) 
    if n%2 == 0 :
        col = n-1 
    elif n%2 != 0 : 
        col = n 
    for i in range(1,n) : 
        if i == 1 or i == n : 
            print(("-" * (((col//2)+1)-i)) + "*" + ("-"*(((col//2)+1)-i)))
        elif i == math.ceil(n/2) :
            print('*' + '-'*(col-2) + '*')
            if n%2 == 0 :
                print('*' + '-'*(col-2) + '*')
        else : 
            print('-'*((col//2)+1-i) + '*' + '-'*(2*(col-i)) + '*' + '-'*((col//2)+1-i))
  
n = input()
star(n)  

