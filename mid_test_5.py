import math

a = 0.01
b = 0.005
c = 0.00001
d = 0.01

rab = int(input("Enter number of rabbits: "))
wol = int(input("Enter number of wolves: "))
day = int(input("Enter number of days to simulate: "))
print()
i = 1

while i <= day:
    rab_next =  (1 + a) * rab - c * rab * wol
    wol_next = (1 - b) * wol + c * d *rab * wol
    rab_next = math.floor(rab_next)
    wol_next = math.floor(wol_next)
    print(f'The rabbit population after day {i}: {rab_next}')
    print(f'The wolve population after day {i}: {wol_next}')
    print()
    rab = rab_next
    wol = wol_next
    i += 1
