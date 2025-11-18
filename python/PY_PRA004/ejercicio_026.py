def rectangulo(alto, ancho, sinbolo):
    for i in range(int(alto)):
        if i == 0 or i == int(alto)-1:
            for i in range(int(ancho)):
                print(f" {sinbolo} ", end="")
            print("")
        else:
            print(f" {sinbolo} ", end="")
            for i in range(int(ancho)-2):
                print(f"   ", end="")
            print(f" {sinbolo} ", end="")
            print("")




ancho = input("Introduce un numero para el ancho: ")
alto = input("Introduce un numero para el alto: ")
simbolo = input("Introduce un simbolo o pulsa enter para *: ")
if simbolo == "":
    simbolo ="*"
rectangulo (alto, ancho, simbolo)   