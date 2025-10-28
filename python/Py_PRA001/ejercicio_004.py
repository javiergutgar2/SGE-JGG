altura = input("¿Cuanto mides? ")
peso = input("¿Cuantto pesas? ")
imc = float(peso) / (float(altura)*float(altura))
print (f"Tu imc es: {round(imc, 2)}")