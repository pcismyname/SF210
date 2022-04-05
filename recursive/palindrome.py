def is_palindrome(s):
    if len(s) < 2:
        return True  
    else:
        return s[0] == s[-1] and is_palindrome(s[1 : -1])