def count_to_by(n, m):
    if n < 1 or m < 1:
        raise ValueError
    if n <= m:
        print(n,end="")
    else :
        count_to_by (n-m, m)
        print(f", {n}",end='')


count_to_by(10,1)