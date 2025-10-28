productos = {
	"Camiseta": 15,
	"Pantalón": 25,
	"Zapatos": 30,
	"Gorra": 10,
	"Cinturon": 20,
}

precioUsuario = int(input("Introduce un precio: "))

for producto, precioProducto in productos.items():
	if int(precioProducto) < precioUsuario:
		print(f"{producto}: {precioProducto}")