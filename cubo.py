class Cubo:
	def __init__(self):
		self.cara_bl = ["bl", "bl", "bl", "bl", "bl", "bl", "bl", "bl", "bl"] # usar bucles?
		self.cara_na = ["na", "na", "na", "na", "na", "na", "na", "na", "na"] # usar enum para colores?
		self.cara_ve = ["ve", "ve", "ve", "ve", "ve", "ve", "ve", "ve", "ve"]
		self.cara_ro = ["ro", "ro", "ro", "ro", "ro", "ro", "ro", "ro", "ro"]
		self.cara_az = ["az", "az", "az", "az", "az", "az", "az", "az", "az"]
		self.cara_am = ["am", "am", "am", "am", "am", "am", "am", "am", "am"]
		# 0 1 2
		# 3 4 5
		# 6 7 8

		# default: F: verde, U: blanco, R: rojo, ...
		self.posiciones = [self.cara_bl, 
				  self.cara_na, self.cara_ve, self.cara_ro, self.cara_az, 
				  		   self.cara_am]
		
	# función que obtenga la transformación del cubo en función del movimiento + posición del cubo
	# ej. (movimiento R) + (a la derecha está el rojo): (sentido contrario a las agujas del reloj en la cara roja)
	def get_transformacion(self, movimiento):
		match movimiento:
			case "R":
				return self.posiciones[3], "contrarreloj" # enum para sentido? bool?

	def rotar(self, cara, sentido):
		match cara[4]: # hacer clases para las caras?
			case "ro":
				cara[0], cara[1], cara[2], cara[3], cara[5], cara[6], cara[7], cara[8] = cara[6], cara[3], cara[0], cara[7], cara[1], cara[8], cara[5], cara[2]

				aux = self.cara_ve[2], self.cara_ve[5], self.cara_ve[8]
				self.cara_ve[2], self.cara_ve[5], self.cara_ve[8] = self.cara_am[2], self.cara_am[5], self.cara_am[8]
				self.cara_am[2], self.cara_am[5], self.cara_am[8] = self.cara_az[6], self.cara_az[3], self.cara_az[0]
				self.cara_az[6], self.cara_az[3], self.cara_az[0] = self.cara_bl[2], self.cara_bl[5], self.cara_bl[8]
				self.cara_bl[2], self.cara_bl[5], self.cara_bl[8] = aux



	def hacer_movimiento(self, movimiento):
		transformacion = self.get_transformacion(movimiento)
		cara, sentido = transformacion
		self.rotar(cara, sentido)

	def __str__(self):
		return f"{self.cara_bl}\n{self.cara_na}\n{self.cara_ve}\n{self.cara_ro}\n{self.cara_az}\n{self.cara_am}"

	def __repr__(self):
		return self.__str__()


if __name__ == '__main__':
	cubo = Cubo()
	print(cubo)
	cubo.hacer_movimiento("R")
	print()
	print(cubo)
