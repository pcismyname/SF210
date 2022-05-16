def exam_stats(file):
    with open (file,'r') as f:
        data = f.read()
        data = [float(i) for i in data.split()]
        if len(data) == 0:
             return
        print(f"{len(data)} scores, average = {sum(data)/len(data):.1f}")
        print(f"max: {max(data)}, min: {min(data)}")


print((0.1+0.2))

exam_stats("Final\scores.txt")
