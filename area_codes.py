def area_codes(file):
    with open (file,'r') as f:
        data = [i.strip('\n') for i in f.readlines()]
        code = [i.split('-') for i in data]
        dict = {i[0] : 0 for i in [j for j in code]}

        code2 = [int(i[0]+i[1]+i[2]) for i in code]
        code2.sort() 
        code3 =[str(i) for i in code2]
        code4 = [i[:3]+'-'+i[3:6]+'-' +i[6:] for i in code3]   
        if len(code4) == 1:
           print(data[0])
           return
        
        print(code4)
        print(dict)
        
        for key in dict:
            for i in code:
                if key  == i[0]:
                    dict[key] += 1
        #print(dict)
        value = dict.values()
        max_num = max(value)
        count = 0

        for i in code4:
            for key in dict:
                if dict[key] == max_num and i[0:3] == key and count<max_num:
                    print(i)
                    count += 1      
                   
area_codes('file/codes.txt')