class Calculator: #teen klassi
    def add(self, a, b):
        return a + b # teen liitmis funktsiooni

    def subtract(self, a, b):
        return a - b # lahutamis funktsioon

    def multiply(self, a, b):
        return a * b #korrutamis funktsioon

    def divide(self, a, b):
        return a / b #jagamis funktsioon


my_cl = Calculator()

while True: # kui tõene siis trükib välja 5 erinevat valikut

    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Exit")

    ch = int(input("Select operation: ")) #kasutaja sisestab millist varjanti ta tahab kasutada


    if ch in (1, 2, 3, 4, 5):


        if (ch == 5):
            break # kui kasutaja valib varjandi 5 siis lõpetab


        a = int(input("Enter first number: ")) # küsib kasutaja käest numbrit
        b = int(input("Enter second number: ")) # üsib kasutaja käest teist numbrit

        if (ch == 1):
            print(a, "+", b, "=", my_cl.add(a, b)) # kui ta valis varjant 1 siis liidab need numbrid
        elif (ch == 2):
            print(a, "-", b, "=", my_cl.subtract(a, b))# varjant 2 korral lahutab numbrid
        elif (ch == 3):
            print(a, "*", b, "=", my_cl.multiply(a, b))# varjant 3 korral korrutab numbrid
        elif (ch == 4):
            print(a, "/", b, "=", my_cl.divide(a, b))# varjant 4 korral jagab numbrid

    else:
        print("Invalid Input")#kui midagi muud siis ütleb "Invalid Input"