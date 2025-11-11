C = 7500
x = 4
n = 10
def calcular_beneficio(capital, tasa, anyos):
    total = capital * (1 + (tasa/100))**anyos
    return total

Cn = calcular_beneficio(C, x, n)

print(f"El beneficio final después de {n} años será: {Cn:.2f}€")