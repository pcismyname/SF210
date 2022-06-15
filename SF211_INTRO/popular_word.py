def popular_words(text: str, words: list) -> dict:
    ans = dict()
    for i in words:
        ans[i] = 0
    for i in text.split():
        if i.lower() in words:
            ans[i.lower()] += 1
    return ans
    


print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))