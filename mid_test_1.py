def pi(n):
    if n == 1:
        return 3
    sum  = 3
    for i in range(1,n):
        deno = i * 2
        if i % 2 == 0:
            sum -= 4/(deno*(deno+1)*(deno+2))
        else :
            sum += 4/(deno*(deno+1)*(deno+2)) 
    return sum           


print(pi(2))