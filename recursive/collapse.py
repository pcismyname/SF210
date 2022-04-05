def collapse_sequences(seq,char):
    if len(seq) < 2:
        return seq
    else :
        if seq[0] == char and seq[1] == char:
            return collapse_sequences(seq[1:], char)
        else:
            return seq[0] +  collapse_sequences(seq[1:], char)
