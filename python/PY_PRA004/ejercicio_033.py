def contar_letras_numeros(texto):
    digitos = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    diccionario = {
        "letras": 0, 
        "numeros": 0
        }
    for caracter in texto:
        if caracter in digitos:
            diccionario["numeros"] = diccionario["numeros"] + 1
        else:
            diccionario["letras"] = diccionario["letras"] + 1
            
    return diccionario

print(f"{contar_letras_numeros("Python 3.10")}")
print(f"{contar_letras_numeros("La conferencia empezará a las 10:30 y terminará a las 18:45")}")
print(f"{contar_letras_numeros("Hoy 16/11/2025 vamos a practicar Python")}")