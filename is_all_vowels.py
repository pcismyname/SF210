def is_all_vowels(word):
    check = True
    word = word.lower()
    vowel = ['a','e','i','o','u']
    for i in word:
        if i >= 'a' and i <= 'z':
            if i not in vowel:
                return False
    return True


print(is_all_vowels('"ei_e_io"'))

