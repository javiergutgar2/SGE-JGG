def formatear_decimales(decimales=2):
    def decorador(func):
        def wrapper(*args, **kwargs):
            resultado = func(*args, **kwargs)   
            print(round(resultado, decimales))  
            return resultado
        return wrapper
    return decorador


@formatear_decimales(3)
def dividir(a, b):
    return a / b

@formatear_decimales()
def calcular_precio_final(subtotal, iva):
    return subtotal * (1 + iva)


dividir(10, 3)                
calcular_precio_final(100, 0.21)  