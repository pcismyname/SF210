def is_magic_square(mat):
    sol = []
    for i in range(len(mat)):
        if len(mat) != len(mat[i]):
            return False
    for i in range(len(mat)):
        sum = 0
        for j in range(len(mat[0])):
            sum += mat[i][j]
        sol.append(sum)
        sum = 0
        for j in range(len(mat[0])):
            sum += mat[j][i]
        sol.append(sum)
        sum = 0
        for j in range(len(mat[0])):
            sum +=  mat[j][len(mat)-i-1]
        sol.append(sum)
        sum = 0
        for j in range(len(mat[0])):
            sum +=  mat[j][j]
        sol.append(sum)
    for i in sol :
        if i != sol[1]:
            return False
    return True    