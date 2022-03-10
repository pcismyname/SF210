def check_dates(file):
    full = 'differ by one full month or more!'
    one = 'are within one month of each other.'
    with open(file, 'r') as f:
        for line in f.readlines():
            data = line.split()
            day1, month1 = int(data[1]), int(data[0])
            day2, month2 = int(data[3]), int(data[2])
            if abs(month2 - month1) > 1:
                print(f'{month1}/{day1} and {month2}/{day2} {full}')
            elif month1 == month2:
                print(f'{month1}/{day1} and {month2}/{day2} {one}')
            else:
                if month1 > month2:
                    tday1, tday2 = day2, day1
                    if tday2 >= tday1:
                        print(f'{month1}/{day1} and {month2}/{day2} {full}')
                    else :
                        print(f'{month1}/{day1} and {month2}/{day2} {one}')
                elif abs(month1 - month2) <= 1:
                    if day2 >= day1:
                        print(f'{month1}/{day1} and {month2}/{day2} {full}')
                    else :
                        print(f'{month1}/{day1} and {month2}/{day2} {one}')

check_dates('file/dates.txt')
            




