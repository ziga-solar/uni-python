from random import *

ana = 1
berta = 1

def met(total, ime):
    while True:
        roll = randint(1, 6)
        total = premik(roll, total, ime)

        if roll != 6 or total >= 30:
            return total

def premik(roll, total, ime):
    print(ime, "je vrgla", roll, "in je na polju", total+roll)
    return total + roll

while True:
    ana = met(ana, "Ana")

    if ana >= 30:
        print("Ana je zmagala")
        break

    elif ana == berta:
        print("Berta gre na začetek")
        berta = 1

    berta = met(berta, "Berta")

    if berta >= 30:
        print("Berta je zmagala")
        break

    elif berta == ana:
        print("Ana gre na začetek")
        ana = 1
