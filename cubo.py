class Cubo:
	def __init__(self):
		self.cara_bl = ["bl", "bl", "bl", "bl", "bl", "bl", "bl", "bl", "bl"]
		self.cara_na = ["na", "na", "na", "na", "na", "na", "na", "na", "na"]
		self.cara_ve = ["ve", "ve", "ve", "ve", "ve", "ve", "ve", "ve", "ve"]
		self.cara_ro = ["ro", "ro", "ro", "ro", "ro", "ro", "ro", "ro", "ro"]
		self.cara_az = ["az", "az", "az", "az", "az", "az", "az", "az", "az"]
		self.cara_am = ["am", "am", "am", "am", "am", "am", "am", "am", "am"]
		# 0 1 2
		# 3 4 5
		# 6 7 8

		# default: F: verde, U: blanco, R: rojo, ...
		self.posiciones = [cara_bl, 
				  cara_na, cara_ve, cara_ro, cara_az, 
				  		   cara_am]
		
	# función que obtenga la transformación del cubo en función del movimiento + posición del cubo
	# ej. (movimiento R) + (a la derecha está el rojo): (sentido contrario a las agujas del reloj en la cara roja)
	def get_transformacion(movimiento):
		match movimiento:
			case "R":
				return self.posiciones[3], "contrarreloj"

	def rotar(cara, sentido):
		pass

	def hacer_movimiento(movimiento):
		transformacion = self.get_transformacion(movimiento)
		cara, sentido = transformacion
		self.rotar(cara, sentido)
