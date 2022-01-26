def box_of_stars(w,h):
    for i in range(1, h+1):
        for j in range(1, w+1):
            if i == 1 or i == h:
                print("*",end="")
            elif j == 1 or j == w:
                print("*",end="")
            else :
                print(" ",end="")
        print()

box_of_stars(8,5)
