def validar_requeridos(**kwargs):
    obligatorios = ["nombre", "email", "telefono"]
    campos_recibidos = set(kwargs.keys())
    falta = []

    for campo in obligatorios:
        if campo not in campos_recibidos:
            falta.append(f"Falta el campo: {campo}")
    return falta


validacion = validar_requeridos(nombre= "Javier G", edad= 30, ciudad= "Aranda")
for dato in validacion:
    print(dato)