from itertools import permutations

def checkio(crossword, words):

    aval = []
    for i in range(len(crossword)):
        if i%2 == 0:
            for j in range(len(crossword[i])):
                    aval.append(crossword[i][j])

    for i in range(len(crossword)):
        if i%2 ==0:
            for j in range(len(crossword[i])):
                    aval.append(crossword[j][i])
    #print()

    all_alpha = set()
    for word in words:
        for j in word:
            all_alpha.add(j)
    len_all_alpha = len(all_alpha)
    #print(all_alpha)

    scrambles = []
    for word_list in permutations(words):
        temp_char= []
        for word in word_list:
            for char in word:
                temp_char.append(char)
        match = set(zip(aval,temp_char))
        scrambles.append(match)
    #print(scrambles)

    final = dict()
    for answer in scrambles:
        if len_all_alpha == len(answer):
            for num,alpha in answer:
                final[num] = alpha
    #print(final)
    sol = []
    for row in crossword:
        temp = []
        for col in row:
            if col != 0:
                temp.append(final[col])
            else :
                temp.append(" ")
        sol.append(temp)
    
    return sol

    







print(checkio(
        [
            [21, 6, 25, 25, 17],
            [14, 0, 6, 0, 2],
            [1, 11, 16, 1, 17],
            [11, 0, 16, 0, 5],
            [26, 3, 14, 20, 6],
        ],
        ["hello", "habit", "lemma", "ozone", "bimbo", "trace"],
    ) == [
        ["h", "e", "l", "l", "o"],
        ["a", " ", "e", " ", "z"],
        ["b", "i", "m", "b", "o"],
        ["i", " ", "m", " ", "n"],
        ["t", "r", "a", "c", "e"],
    ])