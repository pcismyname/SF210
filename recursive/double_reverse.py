def double_reverse(word):
    if len(word) == 0:
        print("",end="")
    else :
        print(word[-1]+word[-1],end="")
        double_reverse(word[:-1])


print(double_reverse("hello")) 