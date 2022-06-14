def split_pairs(a):
    new = []
    if len(a)%2 == 0:
        for i in range(0,len(a),2):
            new.append(a[i]+a[i+1])
    else:
        for i in range(0,len(a)-1,2):
            new.append(a[i]+a[i+1])
        new.append(a[len(a)-1]+'-')     
    return new

print(split_pairs('abcd') == ['ab', 'cd'])
print(split_pairs('abc'))
