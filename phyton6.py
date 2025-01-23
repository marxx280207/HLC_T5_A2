palabra = input("Ingrese una palabra: ")

if '@' in palabra:
    print("La palabra contiene el símbolo @.")
if '#' in palabra:
    print("La palabra contiene el símbolo #.")
if '$' in palabra:
    print("La palabra contiene el símbolo $.")
if '%' in palabra:
    print("La palabra contiene el símbolo %.")
else:
    print("La palabra no contiene ningún símbolo especial.")
