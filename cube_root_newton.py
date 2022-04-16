def func(iter,num):
    ans = ((iter)**3 - num) / (3* ((iter)**(2)))
    return ans

x = int(input('Enter a number: '))

sum = 0.5
iter = 0.5
for i in range(1000):
    sum -= func(iter,x)
    iter = sum


print(sum)