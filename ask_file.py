
def ask_file_name():
    while True:
        name = input('Type a file name: ')
        try:
            f = open(name) 
        except OSError:
            continue

        return name