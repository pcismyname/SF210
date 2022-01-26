month = [31,28,31,30,31,30,31,31,30,31,30,31]

def ask():
    m = int(input("What is the month (1-12)? " ))
    d = md(m)
    c = 0
    for i in range(0,m-1) :
       c += month[i] 
    print(f'{m}/{d} is day #{c+d} of 365.')
    print()
    return c+d

def md(m):
    if month[m-1] == 31:
        d = int(input("What is the day   (1-31)? " ))
    elif month[m-1] == 30:
        d = int(input("What is the day   (1-30)? " ))
    else :
        d = int(input("What is the day   (1-28)? " ))
    return d

def main():
    print("This program tells you how many days\nit will be until your next birthday.")
    print("Please enter today's date:")
    a=ask()
    print("Please enter your birthday:")
    b=ask()
    bd = (b-a)%365
    if bd == 1 :
        print("Wow,·your·birthday·is·tomorrow!")
    elif bd == 0 :
        print("Happy birthday!")
    else :
        print(f'Your next birthday is in {(b-a)%365} days.')

main()