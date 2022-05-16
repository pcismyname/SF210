import random

def slotMachine():
    data = ["@", "#", "$","&", "*", "x","+"]
    result= ""
    for i in range(3):
        result += random.choice(data)
    return result
    
def isWin(lucky):
    return ((lucky[0]==lucky[1]) and lucky[0]==lucky[2])