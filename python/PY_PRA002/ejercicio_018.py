lista = [1, 2, 2, 3, 4, 4, 5,5,5,5,5,5,5,5,5]
lista2 = ['Peras', 'Plátanos', 'Manzanas', 'Naranjas', 'Peras', 'Naranjas', 'Uvas', 'Uvas']

def eliminar_duplicados(lista_eliminar):
	duplicado = True
	while duplicado:
		duplicado = False
		for dato in lista_eliminar:
			if lista_eliminar.count(dato) >= 2:
				lista_eliminar.remove(dato)
				duplicado = True
	print(f'Lista sin duplicados: {lista_eliminar}')
	
					

eliminar_duplicados(lista)
eliminar_duplicados(lista2)
