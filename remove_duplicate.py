def remove_duplicates(seq):
    seen = set()
    seen_add = seen.add
    new = [x for x in seq if not (x in seen or seen_add(x))]
    seq = new.copy()
    return new

print(remove_duplicates([4, 0, 2, 9, 4, 7, 2, 0, 0, 9, 6, 6]))