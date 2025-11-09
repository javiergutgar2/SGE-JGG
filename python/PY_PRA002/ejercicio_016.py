def calcular_total(precio, iva=21):
	if iva is None:
		total = precio + (precio * 21 / 100)
	else:
		total = precio + (precio * iva / 100)
	print (total)

calcular_total(7500, 4)
calcular_total(12260, 10)
calcular_total(927,)