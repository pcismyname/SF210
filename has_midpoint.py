def has_midpoint(a,b,c):
    mid = False
    if (a+b)/2 == c:
        mid = True
    if (b+c)/2 == a:
        mid =  True 
    if  (a+c)/2==b:
        mid = True

    return mid