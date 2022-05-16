def word_list(file):
    with open (file,'r') as f:
        data = f.read().split()
        book = {}
        for i in data:
            if i[0] not in book:
                book[i[0]] = [i]
            else:
                book[i[0]].append(i)
        for i in book:
            book[i]=sorted(book[i])
        print(book)


word_list("Final\words.txt")
