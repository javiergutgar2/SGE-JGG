datos1 = [100, 10, "sum"]
datos2 = [13, 24, "resta"]
datos3 = [3, 40, "multiplicacion"]
datos4 = [1500, 0, "division"]
datos5 = [100, 3, "division"]


def calcular_resultado (numero1,numero2,operador):
    print (f"Número 1: {numero1}, Número 2: {numero2}: Operación: {operador}")
    if numero1 == 0 or numero2 == 0:
        operador = "otro"
    match operador:
        case "suma":
            print (f"Resultado: {numero1 + numero2}")
        case "resta":
            print (f"Resultado: {numero1 - numero2}")
        case "multiplicacion":
            print (f"Resultado: {numero1 * numero2}")
        case "division":
            print (f"Resultado: {numero1 / numero2}")
        case _:
            print ("Uno de los datos introducidos no es valido")


calcular_resultado(datos1[0],datos1[1],datos1[2])
calcular_resultado(datos2[0],datos2[1],datos2[2])
calcular_resultado(datos3[0],datos3[1],datos3[2])
calcular_resultado(datos4[0],datos4[1],datos4[2])
calcular_resultado(datos5[0],datos5[1],datos5[2])
    