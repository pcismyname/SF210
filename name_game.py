def lyric(word):
    print(f'{word}, {word}, bo-B{word[1:]}')
    print(f'Banana-fana fo-F{word[1:]}')
    print(f'Fee-fi-mo-M{word[1:]}')
    print(f'{word.upper()}!')
    print()

name = input('What is your name? ').split()
lyric(name[0])
lyric(name[1])