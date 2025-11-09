temperaturasA = [5.2, 4.8, -1, 3.9, 2.7, 4.3, 5]
temperaturasB = [26, 26.8, 27, 25, 27.5, 27, 30, 28, 27.5]

def calcular_temperaturas(temperaturasCalcular):
    maxima = max(temperaturasCalcular)
    minima = min(temperaturasCalcular)
    media = sum(temperaturasCalcular) / len(temperaturasCalcular)
    tupla_temperaturas = (media, maxima, minima)
    print(tupla_temperaturas)


calcular_temperaturas(temperaturasA)
calcular_temperaturas(temperaturasB)