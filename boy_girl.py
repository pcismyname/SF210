def boy_girl(file):
    with open (file,'r') as f:
        bsum, gsum = 0, 0
        i = 0
        bc = 0 
        gc = 0
        for line in f.readlines():
            _, age = line.split()
            if i % 2 == 0:
                bsum += int(age)
                bc += 1
            else :
                gsum += int(age)
                gc += 1
            i += 1
        print(f'{bc} boys {gc} girls')
        print(f"Difference between boys' and girls' sums: {abs(bsum-gsum)}")


boy_girl('file/boy_girl.txt')
