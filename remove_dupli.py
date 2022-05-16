def remove_duplicates(word):
    rng = len(word)
    new = ""
    for i in range(rng):
        if  new != "" and (new[-1] == word[i]):
            continue
        new += word[i]
    return new
            
            

print(remove_duplicates('bookkeeeeeper'))
