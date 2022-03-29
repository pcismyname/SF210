def by_age(dict, age_min, age_max):
    new = {}  
    for key in dict:
        if age_max >= dict[key] >= age_min:
            new[dict[key]]  = ''
    for key in dict:
        if  dict[key] in list(new.keys()) :
            new[dict[key]] += key + ' and '
    for key in new:
        new[key] = new[key][:-5]
    return new
  


print(by_age({'Allison': 18, 'Benson': 48, 'David': 20, 'Erik': 20, 'Galen': 15, 'Grace': 25, 'Helene': 40, 'Janette': 18, 'Jessica': 35, 'Marty': 35, 'Paul': 28, 'Sara': 15, 'Stuart': 98, 'Tyler': 6, 'Zack': 20}, 16, 25))
