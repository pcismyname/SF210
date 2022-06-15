def checkio(game_result):
    for i in range(3):
        c = 0
        for j in range(2):
            if game_result[i][j] == '.':
                break
            if game_result[i][j] == game_result[i][j+1]:
                c += 1
            if c == 2:
                return game_result[i][j]
        c = 0
        for j in range(2):
            if game_result[j][i] == '.':
                break
            if game_result[j][i] == game_result[j+1][i]:
                c += 1
            if c == 2:
                return game_result[j][i]
        if game_result[0][0] == game_result[1][1] and game_result[1][1] == game_result[2][2] and game_result[1][1] !='.':
                return game_result[0][0]
        if game_result[0][2] == game_result[1][1] and game_result[2][0] == game_result[1][1] and game_result[1][1] !='.':
                return game_result[0][2]
    return "D"
        

print(checkio([
    "X.O",
    "XX.",
    "OOX"]))
print(checkio([
    "OO.",
    "XOX",
    "XOX"]))
print(checkio([
    "OXO",
    "XOO",
    "OXX"]))
   