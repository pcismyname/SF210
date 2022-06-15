def second_index(text: str, symbol: str):
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    c = 0
    for i in range(len(text)):
        if text[i] == symbol:
            c += 1
        if c== 2:
            return i
    return None