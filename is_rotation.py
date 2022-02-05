def is_rotation(word1, word2):
    if word1 == '' and word2 == '':
        return True
    for i in range(len(word1)):
        new = word1[-i:] + word1[:-i]
        if word2 == new:
            return True
    return False


print(is_rotation("abcde", "deabc"))