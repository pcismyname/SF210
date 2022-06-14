def first_word(text: str) -> str:
    """
    returns the first word in a given text.
    """
    # your code here
    first = ""
    flag = 0
    for i in first_word:
        if i.isalpha():
            flag = 1
        if flag:
            first += i
    return first