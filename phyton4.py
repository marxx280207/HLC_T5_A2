contraseñabn = "secreta123"
intentos = 3

while intentos > 0:
    contraseñain = input("Ingresa la contraseña: ")
    
    if contraseñain == contraseñabn:
        print("¡Bienvenido!")
        break
    else:
        intentos -= 1
        if intentos > 0:
            print("Contraseña incorrecta. Te quedan ",intentos,"intentos.")
        else:
            print("¡Cuenta bloqueada!")