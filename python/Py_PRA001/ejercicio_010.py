def tabla(numero):
    for i in range (11):
        print(f"{numero} x {i} = {numero*i}")
    
entrada = input("Introduce un número para que te muestre la tabla: ")
numero = int(entrada)
tabla(numero)
