def recursion10(x):
    print(x, end= " ")
    if x <= 1:
        print("END ", end ="")
    elif x % 2 == 0:
        recursion10(x//2)
        print("+ ",end="")
    else:
        print("[ ",end="")
        recursion10(3*x+1)
        print("] ",end="")

recursion10(1)
print()
recursion10(4)
print()
recursion10(3)

