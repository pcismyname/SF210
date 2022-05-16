def is_vowel(a):
    for i in a:
        if i not in 'aeiou':
            return False
    return True

print(is_vowel("obama"))  