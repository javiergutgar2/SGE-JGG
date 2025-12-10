def mensaje_inicio(func):
    def wrapper(*args, **kwargs):
        print("Ejecutando función…")
        return func(*args, **kwargs)
    return wrapper

@mensaje_inicio
def sumar(a, b):
    return a + b

resultado = sumar(10, 3)
print("Resultado:", resultado)