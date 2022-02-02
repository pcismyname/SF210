def decimal_to_binary(num):
    bi = []
    while num > 0:
        bi.append(num%2)
        num = num//2
    power = len(bi)-1
    binary = 0
    for i in range(len(bi)-1,-1,-1):
        binary += bi[i]*(10**power)
        power -= 1
    return binary

print(decimal_to_binary(17))