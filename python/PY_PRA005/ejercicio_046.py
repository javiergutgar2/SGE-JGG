def imprimir_estructura(**kwargs):
    for clave, dato in sorted(kwargs.items()):
        print(f"{clave}: {dato}")

imprimir_estructura(perro="dalmata", casa="propiedad", coche="alquilado")