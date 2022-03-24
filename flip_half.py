'''[1, 8, 7, 2, 9, 18, 12, 0]'''
'''8 2 18 0'''
'''0 18 2 8'''
'''[1, 0, 7, 18, 9, 2, 12, 8]'''

def flip_half(num_list):
    temp = [num_list[i] for i in range(len(num_list)) if i%2 != 0]
    for i in range(len(num_list)):
        if i%2 != 0:
            num_list[i] = temp[len(temp)-1-int(i/2)]
    print(num_list)

flip_half([1, 8, 7, 2, 9, 18, 12, 0])
            


    

