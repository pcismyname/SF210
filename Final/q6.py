def maxAll(data):
    if len(list(data)) == 1 and (isinstance(list(data)[0], int) or isinstance(list(data)[0], float)):
       return list(data)[0]
    elif len(list(data)) == 1:
      return maxAll(list(data)[0])
    elif (isinstance(data[0], int) or isinstance(list(data)[0], float)):
      if list(data)[0] > maxAll(list(data)[1:]):
          return list(data)[0]
      else :
          return maxAll(list(data)[1:])
    else:
        return maxAll(list(data)[1:])



print(maxAll( [0, 1, 2, 3] ) == 3)
print(maxAll( [[2],[3]] ) == 3)
print(maxAll( [0, 1, 2, [3, 4], [5]] ) == 5)
print( maxAll([[[[[1, 1], 1], 1], 1], 1]) == 1)
print(maxAll( [2.5, [1, 1.2], [4.2, 1]] ) == 4.2)
print(maxAll( [range(1, 5), {1: 2}, {3}] ) == 4)
print(max({1:1, 2:3})==2)
