def check_command(command):
    command = command.split()
    task = command[0].lower()
    room_id = command[1]
    start = command[2]
    stop = command[3]
    if 'create room' in  task:
        print('hi')
    elif task in ' book':
        print('hi')
    elif task in 'caccel':
        print('hello')
    



lines = int(input())



for i in range(lines):
    commanad = input()
    check_command(commanad)
