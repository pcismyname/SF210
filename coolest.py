

def coolest(file):
    with open(file,'r') as f:
        follower = {}
        with open(file) as f:
            for line in f:
                name1, name2 = line.split()
                if name2 in follower:
                    follower[name2].append(name1)
                else:
                    follower[name2] = [name1]
                
        most_popular = ""
        popularity = -1
        for name, list in follower.items():
            current_popularity = 0
            for n in list:
                if n in follower:
                    current_popularity += len(follower[n])
            if current_popularity > popularity:
                most_popular = name
                popularity = current_popularity
            elif  current_popularity == popularity and name < most_popular:
                most_popular = name


        return most_popular
        


                        
        


print(coolest('file/twitter.txt'))