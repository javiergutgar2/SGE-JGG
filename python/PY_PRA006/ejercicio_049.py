def mensaje_info(func):
    def wrapper(*args, **kwargs):
        print(f"Ejecutando la función: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@mensaje_info
def sumar(a, b):
    return a + b


@mensaje_info
def restar(a, b):
    return a - b


# Uso de las funciones
print("Resultado sumar:", sumar(10, 3))
print("Resultado restar:", restar(10, 3))
