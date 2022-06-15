def first_word(text: str) -> str:
    first = ""
    flag = 0
    for i in text:
        if flag and i.isalpha() != True and i != "'":
            break
        if i.isalpha() :
            flag = 1
        if flag:
            first += i
    return first

print(first_word("Hello world"))
print(first_word("greetings, friends"))
print(first_word("don't touch it"))