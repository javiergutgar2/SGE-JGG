def calcular_bruto_anual(sueldo, pagas):
    pagas_totales = 12 + pagas
    sueldo_bruto = sueldo * pagas_totales
    sueldo2 = round(sueldo_bruto, 2)
    return sueldo2
    

sueldo = int(input("Introduce tu sueldo: "))
pagas = int(input("Introduce el numero de pagas estras '0, 1 ó 2': "))
print(f"Sueldo bruto anual: {calcular_bruto_anual(sueldo, pagas)} €")