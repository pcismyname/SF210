def fibonacci_old(n):
    if n <= 2:
        return 1
    else:
        return fibonacci_old(n - 1) + fibonacci_old(n - 2)



def fibonacci(n,first=0,second=1):
    if n-1 == 0:
        return second
    else :
        new_second = first + second
        first = second
        return fibonacci(n-1,first,new_second)

print(fibonacci_old(5))
print(fibonacci(5))
print(fibonacci(8))
print(fibonacci(10))
