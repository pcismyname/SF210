# sorted(set(seq), key=seq.index)

def remove_duplicates(seq):
    seq[:] = sorted(set(seq), key=seq.index)
    return seq

print(remove_duplicates([4, 0, 2, 9, 4, 7, 2, 0, 0, 9, 6, 6]))
lst = [4, 0, 2, 9, 4, 7, 2, 0, 0, 9, 6, 6]
