def coll(map):
    result = {}
    for k in map.keys():
        v = map[k]
        if k[0] <= v[0]:
            result[k] = v
        else :
            result[v] = k
    print(result)


coll({'two': 'deux', 'five': 'cinq', 'one': 'un', 'three': 'trois', 'four': 'quatre'})
coll({'skate': 'board', 'drive': 'car', 'program': 'computer', 'play': 'computer'})
coll({'siskel': 'ebert', 'girl': 'boy', 'heads': 'tails', 'ready': 'begin', 'first': 'last', 'begin': 'end'}	)
coll({'cotton': 'shirt', 'tree': 'violin', 'seed': 'tree', 'light': 'tree', 'rain': 'cotton'}	)