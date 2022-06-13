import random

def mathQuestion(a, b):
  question = str(random.randint(a, b))
  operands = random.randint(2, 5)
  operators = ['+', '-', '*', '/']
  for i in range(operands-1):
    operator = random.choice(operators)
    operand = str(random.randint(a, b))
    question += f" {operator} {operand}"
  print(question)
  return question

def mathQuiz(n, a, b):
  score = 0
  for i in range(n):
    question = mathQuestion(a, b)
    answer = round(eval(question), 2)
    wrong = 0
    while wrong < 3:
      guess = input(question + ' = ')  
      if eval(guess) != answer:
        print("Wrong. Try again.")
        wrong += 1
      else:
        score += 1
        break
    if wrong == 3:
      print(f"The correct answer is {answer}")
  print(f"Your score is {score}")


def new_equation():
    question = str(random.randint(1,9)) #equation start with number
    operands = random.randint(2,4)
    operators =  ['+', '-', '*', '/']
    for i in range(operands-1):
        operator = random.choice(operators)
        operand = str(random.randint(1, 9))
        question += f" {operator} {operand}"
    return question

print(new_equation())