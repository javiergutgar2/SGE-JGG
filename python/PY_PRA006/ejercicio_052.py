def validar_parametros(*parametros):
    def decorador(func):
        def wrapper(**kwargs):
            faltantes = [p for p in parametros if p not in kwargs]
            if faltantes:
                print(f"Función: {func.__name__}")
                print(f"Faltan los siguientes parámetros: {', '.join(faltantes)}")
            else:
                func(**kwargs)
        return wrapper
    return decorador


@validar_parametros("telefono", "email")
def funcion_1(**kwark):
    print(f"Teléfono: {kwark['telefono']}, Email: {kwark['email']}")


@validar_parametros("nombre", "apellidos", "edad")
def funcion_2(**kwark):
    print(f"{kwark['nombre']} {kwark['apellidos']}, {kwark['edad']} años.")


@validar_parametros("mensaje")
def funcion_3(**kwark):
    print(kwark['mensaje'])

funcion_1(telefono="600123123", email="user@mail.com")
funcion_2(nombre="Ana", apellidos="López Pérez", edad=30)
funcion_3()
