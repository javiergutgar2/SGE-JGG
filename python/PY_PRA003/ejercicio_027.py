def multiplos_de_5():
    total_multiplos = 0
    lista_multiplos = []
    numero = input("Introduce un multiplo de 5: ")
    while numero != "n":
        if int(numero) % 5 == 0:
            total_multiplos += 1
            lista_multiplos.append(numero)
        else:
            print(f"El número introducido: {numero} no es multiplo de 5")
        numero = input("¿Quiéres continuar? Introduce otro multiplode 5 o pulsa N o NO para salir: ")
        if numero == "NO":
            numero = "n"
    print(f"Has escrito {total_multiplos} números múltiplos de 5.")


multiplos_de_5()