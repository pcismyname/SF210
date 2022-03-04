def last_first(name):
    full = name.split()
    print(full)
    return f'{full[1]}, {full[0][0]}.'

print(last_first('Marla Singer'))