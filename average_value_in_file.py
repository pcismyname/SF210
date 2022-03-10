def average_value_in_file(file):
    with open(file,'r') as f:
        line = f.read().split()
        if len(line) == 0:
            return 0.0
        sum = 0
        c = 0
        for i in line:
            c += 1
            sum += float(i)
        return sum/c


average_value_in_file('file/avg_value.txt')