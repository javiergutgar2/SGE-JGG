class Estudiante:
    def __init__(self, nombre, nota_examen, notas_actividades):
        self.nombre = nombre
        self.nota_examen = nota_examen
        self.notas_actividades = notas_actividades

    def nota_media_actividades(self):
        return sum(self.notas_actividades) / len(self.notas_actividades)

    def nota_final(self):
        media_actividades = self.nota_media_actividades()
        return self.nota_examen * 0.7 + media_actividades * 0.3

    def nota_formato(self):
        final = self.nota_final()
        if final < 5:
            return "Insuficiente"
        elif 5 <= final < 6:
            return "Suficiente"
        elif 6 <= final < 7:
            return "Bien"
        elif 7 <= final < 9:
            return "Notable"
        else:  # >= 9
            return "Sobresaliente"

    def esta_aprobado(self):
        return self.nota_final() >= 5

    def mostrar_informe(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota examen: {self.nota_examen}")
        print(f"Promedio actividades: {self.nota_media_actividades():.2f}")
        print(f"Nota final: {self.nota_final():.2f} ({self.nota_formato()})")
        print("Aprobado" if self.esta_aprobado() else "Suspendido")
        print("---------------------")


# Lista de datos
datos = [
    {
        "nombre": "Miguel Ángel Martín",
        "examen": 7.5,
        "actividades": [8.0, 7.2, 6.8, 9.0, 7.5]
    },
    {
        "nombre": "Carlos Cobos",
        "examen": 5.8,
        "actividades": [6.5, 5.7, 6.0, 5.3, 6.2]
    },
    {
        "nombre": "Mario Gómez",
        "examen": 9.0,
        "actividades": [9.5, 8.8, 9.2, 9.0, 8.7]
    },
    {
        "nombre": "Javier Torres",
        "examen": 4.3,
        "actividades": [4.5, 5.0, 3.8, 4.2, 4.7]
    }
]

for dato in datos:
    estudiante = Estudiante(dato["nombre"], dato["examen"], dato["actividades"])
    estudiante.mostrar_informe()
