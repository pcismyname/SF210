# -------------------------
def start_test():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")


# -------------------------


questions = {
 "1.Find the intigral of 3x^2+3x+1 ": "A",
 "2.The formula for a function y=f(x) is f(x)=2x^4, x<=0. Find a formula for f^-1": "B",
 "3.Suppose that the range of g lies in the domain of f so that the composite fg is defined. If f and g are​ one-to-one, can anything be said about f​g? Give a reason for the answer?: ": "A",
 "4.Find the indicated derivative if y=5x^(3/2): ": "B",
 "5.Find the intigral of 4x^3+2x+1 ": "B",
 "6.Find the indicated derivative at x=-2 if y=1-4x^2: ": "C",
 "7.Find the slope of the tangent line f(x)=3x+5/x: ": "D",
 "8.Find the slope of the tangent line f(x)=5t^3-t^2, at t=8: ": "A",
    
}

options = [["A. x^3+3x^2/2+1x+c", "B. x^3+3x^2/2+1x", "C. 2x^4+5x^2/2+1x+c ", "D. x^3+3x^2/2+1 "],
          ["A. 1989", "B. -[(x/2)]^(1/4) ", "C. x^2/3-2x-3", "D. 3x^3-2"],
          ["A. Since f and g are one-to-one ​ FoG is one-to-one, fg is​ one-to-one.", "B.Since f and g are​ one-to-one,f isone-to-one .", "C. Since f and g are inverse functions of each​ other, fg=gf.", "D. Since f is an inverse function of​ g, f​g(x)=x."],
          ["A. 23x-3","B. (15/2)(x)^1/2", "C. x^2/3-2x-3", "D.No answer?"],
          ["A. 3x^2/2+1/2x+c", "B. x^4+x^2/2+1x+c", "C. 2x^4+5x^2/2+1x+c ", "D. x^3+3x^2/4+5 "],
          ["A. 16","2", "C. 16", "D.20"],
          ["A. 43","2", "C. 16", "D.43/16"],
          ["A. 944","B. 572", "C. 166", "D.433"]]

print("ยินดีต้อนรับสู่การสอบ")


start_test()

print("ขอให้โชคดีกับการสอบครั้งต่อไป")