def is_palindrome(list):
    for i in range(int(len(list)/2)):
        if list[i] != list[int(len(list))-i-1]:
            return False
    return True 
    
print(is_palindrome(["alpha", "beta", "gamma", "delta", "gamma", "beta", "alpha"]))