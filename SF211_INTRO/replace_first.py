from tempfile import tempdir


def replace_first(items):
    if items == [] or len(items) == 1:
        return items
    items.append(items[0])
    del items[0]
    return items

print(replace_first([1, 2, 3, 4]))