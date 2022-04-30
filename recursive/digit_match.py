def digit_match(x,y):
    if x < 0 and y < 0:
        raise ValueError
    if len(str(x)) == 1 or len(str(y)) == 1:
        if x == y:
            return 1
        else:
            return 0
    digit1 = x%10
    digit2 = y%10
    if digit1 == digit2:
        return 1 + digit_match(x//10 , y//10)

    return digit_match(x//10,y//10)


print(digit_match(38, 34))
print(digit_match(5, 5552))
print(digit_match(298892, 7892))
print(digit_match(1234567, 67))
print(0%10)
print(2//10==0)
