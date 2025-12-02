from datetime import * 
def calcular_edad(fecha):
    resto = date.today() - fecha
    edad = round((resto.days /365),0)
    return edad

dia = input("Introduce el día de tu nacimiento: ")
mes = input("Introduce el mes de tu nacimiento: ")
anyo = input("Introduce el año de tu nacimiento: ")
try:
    dia = int(dia)
    mes = int(mes)
    anyo = int(anyo)
except ValueError:
    print ("Debes introducir un número valido")
else:
    fecha = date(anyo,mes,dia)
    print(f"Actualmente tienes: {calcular_edad(fecha)} años")