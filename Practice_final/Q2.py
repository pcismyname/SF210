def sumAll(data):
  try:
    return sum(data)
  except:
    if isinstance(data[0], int):
      return data[0] + sumAll(data[1:])
    elif isinstance(data[0], float):
      return data[0] + sumAll(data[1:])
    else:
      return sumAll(data[0]) + sumAll(data[1:])

def main():
  lst = [0, 1, 2, 3]
  print(sumAll(lst))

  lst = [0, 1, 2, [3, 4], 5]
  print(sumAll(lst))

  lst = [[[1, 1], 1, 1], 2]
  print(sumAll(lst))

  lst = [range(1,5),{1:2},{3,3,3}]
  print(sumAll(lst))
main()