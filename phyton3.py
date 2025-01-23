calificacion = int(input("Ingresa una calificación entre 0 y 100: "))
if 0 <= calificacion <= 100:
    if calificacion >= 50:
        print("Aprobado.")
    else:
        print("Reprobado.")
else:
    print("Error: La calificación debe estar entre 0 y 100.")