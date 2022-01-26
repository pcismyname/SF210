def loop_mystery_exam3(x, y):
    z = x + y
    while x > 0 and y > 0 :
        x = x - y
        y -= 1
        print(str(x) + " " + str(y) + " ",end ="")
    print(str(y))
    return z

a = loop_mystery_exam3(40, 10)
print(a)