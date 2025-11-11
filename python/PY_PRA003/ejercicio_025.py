def rectangulo(alto, ancho, sinbolo):
    for i in range(int(alto)):
        for i in range(int(ancho)):
            print(f" {sinbolo} ", end="")
        print("")


ancho = input("Introduce un numero para el ancho: ")
alto = input("Introduce un numero para el alto: ")
simbolo = input("Introduce un simbolo o pulsa enter para *: ")
if simbolo == "":
    simbolo ="*"
rectangulo (alto, ancho, simbolo)   