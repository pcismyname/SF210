def recursion_mystery(x, y):
    if y <= 0:
        print("0 ", end="")
    elif x > y:
        print(x, end = " ")
        recursion_mystery(x-y, y)
    else:
        recursion_mystery(x, y-x)
        print(y,end=" ")


recursion_mystery(6, 3)
print()
recursion_mystery(2, 3)
print()
recursion_mystery(5, 8)
print()
recursion_mystery(21, 12)
print()
recursion_mystery(3, 10)