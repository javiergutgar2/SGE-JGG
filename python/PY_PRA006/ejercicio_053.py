from datetime import datetime

class Persona:
    def __init__(self, nombre, apellido, nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento

    def calcular_edad(self):
        año_actual = datetime.now().year
        return año_actual - self.nacimiento

    def __str__(self):
        return f"Hola, me llamo {self.nombre} {self.apellido} y tengo {self.calcular_edad()} años."


persona_1 = Persona("Javier", "Gutiérrez", 1981)
persona_2 = Persona("Erica", "Abad", 1996)  
persona_3 = Persona("Álex", "Gutiérrez", 2014)  

print(persona_1)
print(persona_2)
print(persona_3)
