def contar_mayusculas_minusculas(texto):
    diciconario_letras = {
        "mayusculas": 0,
        "minusculas": 0
    }
    for letra in texto:
        if letra.isupper():
            diciconario_letras["mayusculas"] = diciconario_letras["mayusculas"]+1
        else:
            diciconario_letras["minusculas"] = diciconario_letras["minusculas"]+1
    
    return diciconario_letras


print(f"{contar_mayusculas_minusculas("Python y postgreSQL son muy populares")}")
print(f"{contar_mayusculas_minusculas("Desarrollo - ESP2025")}")