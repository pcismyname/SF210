def is_happy_number(num):
    set_num =  {int(num)}
    sum = 0
    while sum != 1:
        sum = 0
        for i in str(num):
            sum += int(i) **2
        num = sum
        if num in set_num:
            return False 
        set_num.add(sum)
    return True


print(is_happy_number(139))
print(is_happy_number(4))



        
