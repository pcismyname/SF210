def nearest_value(values: set, one: int) -> int:
    sub = []
    for i in values:
        sub.append(abs(abs(one) - abs(i)))
    print(sub)
    for i in values:
        if i == min(sub) + one or i == one -min(sub) :
            return i


print(nearest_value({4, 7, 10, 11, 12, 17}, 9))
print(nearest_value({4, 7, 10, 11, 12, 17}, 8))
print(nearest_value([0,-2],-1))