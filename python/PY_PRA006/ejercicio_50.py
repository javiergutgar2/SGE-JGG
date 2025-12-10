def separador(func):
    def wrapper(*args, **kwargs):
        print("------------------------")
        ejecucion = func(*args, **kwargs)
        print("------------------------")
        return ejecucion
    return wrapper
    



@separador
def saludar(nombre):
    print(f"Hola, {nombre}!")

# Uso de la función
saludar("Miguel Ángel")
saludar("Rodrigo")
