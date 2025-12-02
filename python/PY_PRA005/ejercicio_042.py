from ejercicio_032 import es_bisiesto

uno = int(input("introduce el primer año: "))
dos = int(input("introduce el segundo año: "))

bisiaestos = 0

for anno in range(uno, dos + 1):
    if es_bisiesto(anno):
        print(anno)
        bisiaestos +=1

if bisiaestos > 0:
    print (f"Entre {uno} y {dos} hay {bisiaestos} años bisiestos.")
else:
    print (f"Entre {uno} y {dos} no hay años bisiestos.")