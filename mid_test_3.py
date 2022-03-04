def undouble(s):
    if s == '':
        return s
    new = ''
    new += s[0]
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            continue
        new += s[i]
        
    return new


print(undouble("little"))