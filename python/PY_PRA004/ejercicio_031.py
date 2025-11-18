catalogo = {
    "PC": ["Balatro", "Baldur's Gate 3"],
    "PS5": ["GTA5", "God of War"],
    "Switch": ["Mario Oddysey"]
}
existe_plataforma = True
existe_juego = False
while(True):
    print("1. Añadir videojuego")
    print("2. Borrar videojuego")
    print("3. Listar el catálogo")
    print("4. Salir")
    eleccion = input("¿Cuál es tu elección?: ")
    if eleccion == "1":
        plataforma_introducida = input("¿De que plataforma es el juego a añadir? ")
        juego_introducido = input("¿Qué juego desea añadir? " )
        if plataforma_introducida not in catalogo:
            catalogo[plataforma_introducida] = []
        if juego_introducido not in catalogo[plataforma_introducida]:
            catalogo[plataforma_introducida].append(juego_introducido)
        else:
            print(f'El videojuego "{juego_introducido}" ya esta registrado en "{plataforma_introducida}"')

    if eleccion == "2":
        print("Plataformas: ")
        for plataforma in catalogo:
            print(f"    {plataforma}")
        plataforma_introducida = input("¿De que plataforma es el juego a eliminar? ")
        try:
            if plataforma_introducida in catalogo:
                print(f"Juegos disponibles en: {plataforma_introducida}")
            for juego in catalogo[plataforma_introducida]:
                print(f"    {juego}")
            juego_introducido = input("¿Qué juego desea eliminar? " )
            if juego_introducido in catalogo[plataforma_introducida]:
                catalogo[plataforma_introducida].remove(juego_introducido)
                print(f'Se borró  "{juego_introducido}" de "{plataforma_introducida}"')
                break
            else:
                print(f'El videojuego "{juego_introducido}" no estaba en el catálogo de la plataforma {plataforma_introducida}')
        except:
            print(f"No existe la plataforma {plataforma_introducida}")

    if eleccion == "3":
        for plataforma in catalogo:
            print(f"{plataforma}:", end=" ")
            for juego in catalogo[plataforma]:
                print(f"{juego}", end=", ")
            print("")
    if eleccion == "4":
        print("Fin del programa...")
        break
