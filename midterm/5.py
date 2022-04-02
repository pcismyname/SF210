def revealLetters(s1,s2):
    new = ''
    count = ''
    for i in s1:
        count += i
        for j in s2:
            if i.upper() == j.upper():
                new += i
                break
        if len(new) != len(count):
            new += '_'
        
    return new


print(revealLetters("Pineapple", "pineal"))
print(revealLetters("Pineapple", "aeiou"))

