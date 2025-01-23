num1 = int(input("Introduce un primer número: "))
num2 = int(input("Introduce un segundo número: "))
num3 = int(input("Introduce un tercer número: "))

if num1 > num2 and num1 > num3:
    print(num1, "es el mayor número.")
elif num2 > num1 and num2 > num3:
    print(num2, "es el mayor número.")
elif num3 > num1 and num3 > num2:
    print(num3, "es el mayor número.")
else:

    if num1 == num2 == num3:
        print("Todos los números son iguales:", num1)
    elif num1 == num2 and num1 > num3:
        print("Hay un empate entre los mayores: ",num1," y ",num2)
    elif num1 == num3 and num1 > num2:
        print("Hay un empate entre los mayores:",num1," y ",num3)
    elif num2 == num3 and num2 > num1:
        print("Hay un empate entre los mayores: ",num2," y ",num3)
