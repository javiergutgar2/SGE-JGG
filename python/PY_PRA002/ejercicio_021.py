def es_palindromo(palabra):
    palindromo = True
    palabraA = []
    for i in range(len(palabra)):
        palabraA.append(palabra[i])
    palabraB = list(palabraA)
    palabraB.reverse()
    for i in range(len(palabra)):
        if palabraA[i-1] != palabraB[i-1]:
            palindromo = False
    if palindromo:
        print(f"{palabra} es un palindromo")
        return True
    else:
        print(f"{palabra} no un palindromo")
    return False

palabra = input("Introduce una palabra: ")
es_palindromo(palabra)

