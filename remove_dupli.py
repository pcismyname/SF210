def remove_duplicates(word):
    new = ''
    for i in range(0,len(word)):
        for j in range(i+1,len(word)-1):
            if word[i] == word[j]:
                continue
            

    return word

print(remove_duplicates('bookkeeeeeper'))
