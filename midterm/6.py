def graduation(gpa, credits, honors):
    if credits < 150 or gpa < 2.0:
        return 'not graduating'
    if gpa < 3.6:
        return 'graduating'
    if gpa < 3.8 and honors < 15:
        return 'cum laude'
    elif gpa >= 3.8 and honors < 15:
        return 'magna cum laude'
    if honors > 14 and gpa <  3.8:
        return 'magna cum laude'
    elif gpa >= 3.8 and honors > 14:
        return 'summa cum laude'



print(graduation(3.85,  190,  15))

    