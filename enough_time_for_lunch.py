def enough_time_for_lunch(h1,m1,h2,m2):
    if h2 < h1 :
        return False 
    elif h1 == h2 :
        if m2 - m1 > 44:
            return True
        else :
            return False
    else:
        hour = h2 - h1
        hour *= 60
        hour +=m2 - m1
        if hour >= 45:
            return True
        else : 
            return False
        

print(enough_time_for_lunch (12, 30, 13, 00)	)

