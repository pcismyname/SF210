def factorial(n):
    if n==1 or n==0:
        return 1
    return n * factrial(n-1)

print(factrial(4))