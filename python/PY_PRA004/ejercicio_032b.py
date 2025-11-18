''' Funciones auxiliares'''
def nombre_mes(numero_mes):
    nombre_mes_array = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre",
    }
    nombre_mes = nombre_mes_array.get(numero_mes)
    return nombre_mes

def dias_mes(nombre_mes):
    dias_por_mes = {
        "Enero": 31,
        "Febrero": 28,
        "Marzo": 31,
        "Abril": 30,
        "Mayo": 31,
        "Junio": 30,
        "Julio": 31,
        "Agosto": 31,
        "Septiembre": 30,
        "Octubre": 31,
        "Noviembre": 30,
        "Diciembre": 31,
    }
    dias_mes = dias_por_mes.get(nombre_mes)
    return dias_mes

'''Funciones del ejercicio'''

def es_bisiesto(anno):
    if (anno % 4 == 0):
        if (anno % 100 == 0):
            if (anno % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    


def calcular_dias_mes(mes, anno):
    bisiesto=es_bisiesto(anno)
    dias_mes_saber = dias_mes(nombre_mes(mes))
    if bisiesto and mes == 2:
        dias_mes_saber = int(dias_mes_saber) + 1
    print(f"El mes de {nombre_mes(mes)} tiene: {dias_mes_saber} días")

def validar_fecha(dia, mes, anno):
    if mes > 12:
        return False
    if mes == 2:
        if es_bisiesto(anno):
            if dia <= 29:
                return True
            else:
                return False
        else:
            if dia <= 28:
                return True
            else:
                return False
    else:
        if dia <= dias_mes(nombre_mes(mes)):
            return True
        else:
            return False


def siguiente_dia(dia, mes, anno):
    if validar_fecha(dia, mes, anno):
        if es_bisiesto(anno):
            if dia == dias_mes(nombre_mes(mes))+1:
                nuevo_dia = 1
                nuevo_mes = mes + 1
            else:
                nuevo_dia = dia + 1
                nuevo_mes = mes
        else:
            if dia == dias_mes(nombre_mes(mes)):
                nuevo_dia = 1
                nuevo_mes = mes + 1
            else:
                nuevo_dia = dia + 1
                nuevo_mes = mes
        if nuevo_mes == 13:
            nuevo_mes = 1
            nuevo_anno = anno + 1
        else:
            nuevo_anno = anno
        fecha = (nuevo_dia, nuevo_mes, nuevo_anno)
        return fecha
    else:
        print(f"la fecha {dia}, {mes}, {anno}, no es valida")
    


print(f"{siguiente_dia(28, 2, 2005)}")