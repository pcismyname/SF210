import math
a,b,c = input().split(',')
d = int(a+b+c)-bool(c)*int(a+b)
e = (10**len(c)-bool(c))*10**len(b)
print(10**len(c)-bool(c))
print(d,e)
f = math.gcd(d,e)
print(f)
print(f'{int(d/f)} / {int(e/f)}')