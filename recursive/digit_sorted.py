def digits_sorted(num):
    if len(str(num)) == 1:
        return True
    elif num < 0:
        return digits_sorted(abs(num))
    if num%10 >= num%100//10:
        return digits_sorted(num//10)
    else:
        return False
