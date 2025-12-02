from ejercicio_032 import es_bisiesto

uno = int(input("introduce un año: "))

anyos = 1
dos = uno
while es_bisiesto(dos+1) == False:
    anyos +=1
    dos +=1

print (f"Desde {uno} faltan {anyos} hasta el siguiente bisiesto.")