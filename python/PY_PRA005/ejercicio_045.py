from ejercicio_044 import tirar_dado

numero_objetivo = 0

while numero_objetivo > 50 or numero_objetivo <25:
    numero_objetivo = int(input("Introduce el número objetivo entre 25 y 50: "))

jugador1 = input("introduce tu nombre Jugador 1: ")
jugador2 = input("introduce tu nombre Jugador 2: ")

puntos_jugador1 = 0
puntos_jugador2 = 0
tirada =0
while  True:
    tirada = tirar_dado()
    puntos_jugador1 += tirada
    print(f"El jugador {jugador1} ha sacado un {tirada} y lleva {puntos_jugador1}.")
    if puntos_jugador1 >= numero_objetivo:
        break
    tirada = tirar_dado()
    puntos_jugador2 += tirada
    print(f"El jugador {jugador2} ha sacado un {tirada} y lleva {puntos_jugador2}.")
    if puntos_jugador2 >= numero_objetivo:
        break

if puntos_jugador1 >= puntos_jugador2:
    print(f"El jugador {jugador1} ha ganado con {puntos_jugador1}.")
    print(f"El jugador {jugador2} ha perdido con {puntos_jugador2}.")
else:
    print(f"El jugador {jugador2} ha ganado con {puntos_jugador2}.")
    print(f"El jugador {jugador1} ha perdido con {puntos_jugador1}.")
