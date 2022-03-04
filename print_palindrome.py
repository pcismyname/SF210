def print_palindrome():
    word = input('Type one or more words: ')
    temp = word
    word = word.lower()
    if word == word[::-1]:
        print(f'{temp} is a palindrome!')
    else:
        print(f'{temp} is not a palindrome.')

print_palindrome()
