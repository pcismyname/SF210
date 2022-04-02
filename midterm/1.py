#anweerac@tu.ac.th

def fac(n):
    sum = 1
    for i in range(1,n+1):
        sum *= i
    return sum


def sin(x,n):
    sum = 0.0
    for i in range(n):
        if i%2 ==  0 :
            sum += x**(2*i+1)/fac(2*i+1)
        else :
            sum -= x**(2*i+1)/fac(2*i+1)
    return sum



print(fac(0))
print(sin(1,2))