def asignaturas(asignatura):
    asignaturas_optativas = ("Informática", "Latín", "Griego")
    for asi in asignaturas_optativas:
        if asi == asignatura:
            encontrada = True
            break
        else:
             encontrada = False
    if encontrada:
        print(f"Asignatura elegida: {asignatura}")
    else:
        print(f"La asignatura {asignatura} no está contemplada.")

asignatura = input("Introduce una asignatura optativa: ")
asignaturas(asignatura)