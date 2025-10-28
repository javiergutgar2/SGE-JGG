anno = int(input("Introduce un año para saber si es bisiesto: "))
if (anno % 4 == 0):
	if (anno % 100 == 0):
		if (anno % 400 == 0):
			print(f"El año {anno} es bisiesto")
		else:
			print(f"El año {anno} No bisiesto")
	else:
		print(f"El año {anno} es bisiesto")
else:
	print(f"El año {anno} NO bisiesto")