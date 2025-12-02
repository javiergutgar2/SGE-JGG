edad_para_conducir = {
    "España": 18,
    "Estados Unidos": 16,
    "Japón": 18,
    "Reino Unido": 17
}
edad = int(input("¿Cuál es tu edad?: "))
pais = input("En que pais resides: ")

if pais in edad_para_conducir:
    if int(edad_para_conducir[pais]) <= edad:
        print (f"En {pais}, puedes conducir")
    else:
        print (f"En {pais}, no puedes conducir. La edad mínima es {edad_para_conducir[pais]} años.")
else:
    print ("Lo siento, no tengo información sobre ese país.")
