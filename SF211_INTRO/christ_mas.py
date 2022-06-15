x= int(input("width : "))
y = int(input("height : "))
mid = y//2      
print("Merry Christmas ^_^")
print("Merry Christmas ^_^")
print("Merry Christmas ^_^")
for i in range(x):
    for j in range(y):
        if i == 0 or i == x-1:
            print("*",end="")
        elif j == mid-1 and i == 1:
            print("()",end="")
        elif j==0 or j==y-1:
            print("*",end = "")
        elif j==mid-i and i != 1 :
            print("/",end="")
        elif j==mid+i and i != 1:
            print("\\",end="")
        elif j > mid-i+1 and j < mid+i-1 and mid+i+1 <= y and mid -i-1 >= 0:
            print("x",end= "")
        elif j == mid-1 and mid+i+1 >= y and mid -i-1 <= 0:
            print("||",end="")
        else:
            print(" ",end="")
    print()
print("Merry Christmas ^_^")
print("Merry Christmas ^_^")
print("Merry Christmas ^_^")