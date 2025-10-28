altura = input("¿Cuanto mides? ")
peso = input("¿Cuantto pesas? ")
imc = float(peso) / (float(altura)*float(altura))
print (f"Tu imc es: {round(imc, 2)}")

if imc < 18.5:
    categoria = "Bajo peso"
elif imc < 25:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Sobrepeso"
elif imc < 35:
    categoria = "Obesidad tipo I (leve)"
elif imc < 40:
    categoria = "Obesidad tipo II (moderada)"
else:
    categoria = "Obesidad tipo III (mórbida)"


print (f"De acuerdo a tu IMC, estás en la categoría: {categoria}" )