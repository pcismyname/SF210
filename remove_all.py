def remove_all(word,x):
    new = ''
    for i in word:
        if i == x:
            continue
        else:
            new += i
    return new

print(remove_all('Summer is here !','e'))