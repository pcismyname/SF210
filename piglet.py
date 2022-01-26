import random

print("Welcome to Piglet!")
score = 0
dice_face = [1,2,3,4,5,6]
while(True):
    dice = random.choice(dice_face)
    if dice == 0:
        dice = 6 
    print(f'You rolled a {dice}')
    if dice == 1 :
        print('You got 0 points.')
        break
    else :
        score += dice
    check = input("Roll again? ").upper()
    if check[0] == "N":
        print(f'You got {score} points.')
        break
    else :
        continue
        