def safe_pawns(pawns: set) -> int:
    c = 0
    for i in pawns:
        l = chr(ord(i[0])-1)+str(int(i[1])-1)
        r = chr(ord(i[0])+1)+str(int(i[1])-1)
        c += l in pawns or r in pawns
    return c


print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6)
print(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1)
