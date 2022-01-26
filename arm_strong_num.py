def armstrong_numbers(n):
    begin = pow(10,n-1)
    limit = pow(10,n)
    if n <= 0 :
        return
    if n == 1:
         print(0,end=" ")
    for num in range(begin, limit):
        sum = 0
        temp = num
        while temp > 0 :
            sum += pow(temp%10,n)
            temp //= 10
        if num == sum:
            print(sum,end = " ")


