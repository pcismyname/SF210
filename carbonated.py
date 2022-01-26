def carb(a,b,c):
    print("say",b,"not",c,"or",a)

def main():
    soda = "coke"
    pop = "pepsi"
    coke = "pop"
    pepsi = "soda"
    say = pop

    carb(coke,soda,pop)
    carb(pop,pop,pepsi)

main()