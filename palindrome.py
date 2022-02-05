def is_palindrome(word):
    word = word.lower()
    parin = word[::-1]
    if word == parin:
        return True
    else : 
        return False

print(is_palindrome('dad')) 