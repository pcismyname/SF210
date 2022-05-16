def flip_lines(file):
    with open (file,'r') as f:
        all_line = [line.strip('\n') for line in f.readlines()]
        print(all_line)
        for i in range(1,len(all_line),2):
            print(all_line[i].upper())
            print(all_line[i-1].lower())
        if len(all_line) %2 == 1:
            print(all_line[len(all_line)-1].upper())


flip_lines("file\carroll.txt")
