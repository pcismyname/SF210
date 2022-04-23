from cmath import sqrt


def func(iter,num):
    ans = 0.5
    while ans != num**(1/3):
        ans -= ((iter)**3 - num) / (3* ((iter)**(2)))
        iter = ans
    return ans

x = int(input('Enter a number: '))
print(func(0.5,x))


