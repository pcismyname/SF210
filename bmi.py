print("This program reads data for two people")
print("and computes their body mass index (BMI).")
print()

def ask():
    h = float(input("height (in inches)? "))
    w = float(input("weight (in pounds)? "))
    return h,w

def bmi():
    h,w = ask()
    BMI = w / (h**2) * 703
    print(f'BMI = {BMI:.1f}')
    check(BMI)

def check(BMI):
    if BMI < 18.5 :
        print("class 1")
    elif BMI < 24.5:
        print("class 2")
    elif BMI < 30 :
        print("class 3")
    else :
        print("class 4")
    print()

print("Person 1 information:")
bmi()
print("Person 2 information:")
bmi()
print("Have a nice day!")