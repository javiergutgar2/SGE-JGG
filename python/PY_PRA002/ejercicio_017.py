from datetime import datetime, date

def formatear_fecha(fecha):
	formato = "%Y-%m-%d"
	fecha_fecha = datetime.strptime(fecha, formato)
	fecha_correcta = fecha_fecha.strftime("%d/%m/%Y")
	print(f"Fecha formateada: {fecha_correcta}")
	
formatear_fecha(datetime.today().strftime("%Y-%m-%d"))
formatear_fecha("1995-03-20")
formatear_fecha("2001-09-11")