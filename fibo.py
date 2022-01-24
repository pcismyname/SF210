def fibo(n) :
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)

print("This program lists the Fibonacci sequence.")
max = int(input("Max value? "))

i = 0
ans = []
while(True) :
    if fibo(i) > max :
        break
    ans.append(fibo(i))
    i+=1
    
for i in range (0,len(ans)-1):
    print(ans[i],end = ", ")
print(ans[len(ans)-1])