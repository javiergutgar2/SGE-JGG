estudiantes = (
	("José", 5),
	("Ana",8),
	("Luis",6),
	("María",9),
	("Pedro",4)
)
suma = 0
for estudiante, nota in estudiantes:
	if nota >= 5:
		print(f"Estudiante {estudiante} ha aprobado con la nota: {nota}")