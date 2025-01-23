def dibuja():
    numestrellas=int(input("introduce un rumero"))
    contador=0
    for index in range (numestrellas):
        contador+=1
        estrella="⭐"
        print(estrella*contador)
dibuja()