def convertir_segundos(numero_segundos):
    horas = numero_segundos / 3600
    minutos = numero_segundos % 3600 / 60
    segundos = (numero_segundos % 3600) % 60
    print(f"{numero_segundos:.0f} segundos son {horas:.0f} horas, {minutos:.0f} minutos y {segundos:.0f} segundos")


entrada = input("Introduce un numero de segundos para convertir: ")
segundos = int(entrada)
convertir_segundos(segundos)