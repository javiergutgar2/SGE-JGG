def contar_texto(texto):
    contado ={
    "vocales": 0,
    "consonantes": 0,
    "numeros": 0,
    "espacios": 0
}

    vocales = (
    'a', 'e', 'i', 'o', 'u',
    'á', 'é', 'í', 'ó', 'ú',
    'A', 'E', 'I', 'O', 'U',
    'Á', 'É', 'Í', 'Ó', 'Ú',
    'ü', 'Ü'
)
    consonantes = (
    'b','c','d','f','g','h','j','k','l','m','n','ñ','p','q','r','s','t','v','w','x','y','z',
    'B','C','D','F','G','H','J','K','L','M','N','Ñ','P','Q','R','S','T','V','W','X','Y','Z'
)
    simbolos = 0
    numeros = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    for letra in texto:
        if letra in vocales:
            contado['vocales'] +=1
        if letra in numeros:
            contado['numeros'] +=1
        if letra == " ":
            contado['espacios'] +=1
        if letra in consonantes:
            contado['consonantes'] +=1
        else:
            simbolos +=1
    return contado

print(contar_texto("Python 3.10"))
print(contar_texto("La conferencia empezará a las 10:30 y terminará a las 18:45"))
print(contar_texto("Hoy 16/11/2025 vamos a practicar Python"))
