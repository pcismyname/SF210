
def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    b = 0
    e = len(text)
    if begin in text:
        b = text.index(begin) + len(begin)
    if end in text:
        e = text.index(end)
    return text[b:e]


print(between_markers('No [b]hi', '[b]', '[/b]'))
print()
print()
print()
print()
print()