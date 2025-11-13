def contal_vocales(palabra):
    vocales = ["a", "e", "i", "o", "u"]
    resultado = 0
    for letra in palabra:
        for vocal in vocales:
            if letra.lower() == vocal:
                resultado +=1
                break
    print(f"La cantidad de vocales es: {resultado}")


entrada = input("Introduce una palabra para contar las vocales: ")
contal_vocales(entrada)