def print_range(start,stop):
    for i in range(ord(stop)-ord(start)+1):
        letter = chr(ord(start)+i)
        print(letter,end=" ")
    print()

print_range("e","g")
print_range("n","s")