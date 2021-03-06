def dna_errors(dna_1,dna_2):
    dna_1 = dna_1.upper()
    dna_2 = dna_2.upper()
    error = 0
    
    if len(dna_1) != len(dna_2):
        error += abs(len(dna_1) - len(dna_2))
        if len(dna_1) > len(dna_2):
            dna_1,dna_2 =dna_2,dna_1

    for i in range(0,len(dna_1)):
        if dna_1[i] =='-':
            error += 1
        elif dna_2[i] == '-':
            error += 1
        else:
            if dna_1[i] == 'A':
                if dna_2[i] != 'T':
                    error += 2
            if dna_1[i] == 'T':
                if dna_2[i] != 'A':
                    error += 2
            if dna_1[i] == 'C':
                if dna_2[i] != 'G':
                    error += 2
            if dna_1[i] == 'G':
                if dna_2[i] != 'C':
                    error += 2
    return error

print(dna_errors('GGGA-GAATCTCTGGACT',"CTCTACTTA-AGACCGGTACAGG"))