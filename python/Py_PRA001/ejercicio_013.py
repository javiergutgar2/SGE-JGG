def convertir(pulgadas):
    resultado = pulgadas/2.54
    print(f"{pulgadas} pulgadas son {resultado:.2f} cm.")

entrada = input("Introduce las pulgadas y las pasamos a centimetros: ")
pulgadas = float(entrada)
convertir(pulgadas)