productos = {
    "Leche": 10,
    "Pan": 8,
    "Huevos": 20,
    "Queso": 4,
    "Mantequilla": 6
}
cantidadComprar = 0
for producto in productos:
    cantidadComprar = input(f"¿Cuántas unidades de {producto} quieres comprar?: ")
    if int(cantidadComprar) > int(productos.get(producto)):
        print("hola")
        print(f'No hay suficientes unidades de "{producto}" en inventario. \nSolo hay "{productos.get(producto)}" unidades disponibles.')
    else:
        disponibles = int(productos.get(producto))-int(cantidadComprar)
        productos[producto]= disponibles
        if productos[producto] == 0:
            print(f'¡Atención! El producto "{producto}" se ha agotado.')

for producto in productos:
    print(f"{producto}: {productos.get(producto)} unidades")


