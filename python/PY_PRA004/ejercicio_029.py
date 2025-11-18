def calcular_pesos():
    cantidad = 0
    peso_total = 0
    cantidad_total = 0
    productos = {
        "payaso": 112,
        "muñeca": 75,
        "robot": 250,
        "peluche": 180,
        "puzzle": 400
    }
    for producto in productos:
        cantidad = input(f"Cuantos se ha vendido de {producto}: ")
        peso_total = peso_total + int(cantidad) * int(productos.get(producto))
        cantidad_total = int(cantidad_total) + int(cantidad)

    print(f"Peso total: {peso_total} gr.")
    print(f"Peso medio por producto:  {peso_total/cantidad_total} gr.")


calcular_pesos()