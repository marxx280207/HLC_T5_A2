import random

numero = random.randint(1, 50)

def adivina():
    num = None

    while num != numero:
        num = int(input("Adivina el número (entre 1 y 50): "))

        if num == numero:
            print("¡Correcto!")
        elif num > numero:
            print("Más bajo.")
        else:
            print("Más alto.")

adivina()
