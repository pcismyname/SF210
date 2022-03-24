def get_percent_even(lst):
    if lst == []:
        return
    count = 0
    for i in lst: 
        if i%2 == 0:
            count += 1
    return count/len(lst)*100
