
def divisores(numero):
    lista_divisores =[]
    prueba_divisores = 1
    for i in range(numero):
        if numero % prueba_divisores == 0:
            lista_divisores.append(prueba_divisores)
        prueba_divisores += 1
        if prueba_divisores > numero:
            break
    return lista_divisores

numero_probar = 12
print (f"Lista divisores de {numero_probar}: {divisores(numero_probar)}")
numero_probarB = 18
print (f"Lista divisores de {numero_probarB}: {divisores(numero_probarB)}")