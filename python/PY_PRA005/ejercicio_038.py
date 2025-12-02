def aumento_salario(salario, porcentaje = 2):
    try:
        nuevo_salario = salario * ((100 + int(porcentaje))/100)
    except:
        print("¡No se puede dividir por cero!")
    else:
        return nuevo_salario

salario = input("Introduce tu salario: ")
porcentaje = input ("Intorduce el porcentaje de subida, por defecto el 2%: ")

if porcentaje == "":
    porcentaje= 2

try:
    salario_int = int(salario)
    porcentaje_int =int(porcentaje)
except ValueError:
    print (f"Debes introducir un número válido.")
else:
      print(f"Tu nuevo salario con un aumento del {porcentaje}% es: {aumento_salario(salario_int, porcentaje_int)}€")