import random

def makeSecreteNumber():
  return ''.join(random.sample(list('0123456789'), 4))

def compareNumbers(a, b):
  positions = 0
  digits = 0
  for i in range(4):
    if a[i] == b[i]:
      positions += 1
    if b[i] in a:
      digits += 1
  if digits == 0:
    print('No digits correct.')
  elif positions == 4:
    print('You found the number.')
  else:
    print(f"Correct: {digits} digits, {positions} positions.")

  return positions == 4

def correctGuess(guess):
  return len(set(list(guess))) == 4
  
def guessNumber():
  secretNumer = makeSecreteNumber()
  tries = 0
  while tries < 20:
    guess = input("Enter your guesss: ")
    if not correctGuess(guess):
      print("Please enter 4 different digits. Try again.")
      continue
    if compareNumbers(secretNumer, guess):
      break
    tries += 1
  if tries == 20:
    print(f"The secret number is {secretNumer}")
      

guessNumber()
  