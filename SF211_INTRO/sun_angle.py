def sun(time):
    time_con = time.split(':')
    hour = (int(time_con[0]))
    minute = (int(time_con[1]))
    if hour < 6 or hour > 18 or (hour == 18 and minute > 0):
        return "I don't see the sun!"
    degree = (hour-6)*15
    degree += 0.25*minute
    return degree


sun("07:00")
sun("12:15")
