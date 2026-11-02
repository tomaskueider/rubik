from enum import Enum

class Cubo:
	def __init__(self):
		self.cara_bl = [Color.BLANCO] * 9 
		self.cara_na = [Color.NARANJA] * 9
		self.cara_ve = [Color.VERDE] * 9
		self.cara_ro = [Color.ROJO] * 9
		self.cara_az = [Color.AZUL] * 9
		self.cara_am = [Color.AMARILLO] * 9
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
			case "U":
				return self.posiciones[0], "contrarreloj"
			case "F":
				return self.posiciones[2], "contrarreloj"

	def girar(self, cara, sentido): # prima = False en lugar de sentido?
		match cara[4]: # hacer clases para las caras? cara[4] es el color del centro, identifica a la cara
			case Color.ROJO:
				cara[0], cara[1], cara[2], cara[3], cara[5], cara[6], cara[7], cara[8] = cara[6], cara[3], cara[0], cara[7], cara[1], cara[8], cara[5], cara[2]

				aux = self.cara_ve[2], self.cara_ve[5], self.cara_ve[8]
				self.cara_ve[2], self.cara_ve[5], self.cara_ve[8] = self.cara_am[2], self.cara_am[5], self.cara_am[8]
				self.cara_am[2], self.cara_am[5], self.cara_am[8] = self.cara_az[6], self.cara_az[3], self.cara_az[0]
				self.cara_az[6], self.cara_az[3], self.cara_az[0] = self.cara_bl[2], self.cara_bl[5], self.cara_bl[8]
				self.cara_bl[2], self.cara_bl[5], self.cara_bl[8] = aux

			case Color.BLANCO:
				cara[0], cara[1], cara[2], cara[3], cara[5], cara[6], cara[7], cara[8] = cara[6], cara[3], cara[0], cara[7], cara[1], cara[8], cara[5], cara[2]

				aux = self.cara_ve[0], self.cara_ve[1], self.cara_ve[2]
				self.cara_ve[0], self.cara_ve[1], self.cara_ve[2] = self.cara_ro[0], self.cara_ro[1], self.cara_ro[2]
				self.cara_ro[0], self.cara_ro[1], self.cara_ro[2] = self.cara_az[0], self.cara_az[1], self.cara_az[2]
				self.cara_az[0], self.cara_az[1], self.cara_az[2] = self.cara_na[0], self.cara_na[1], self.cara_na[2]
				self.cara_na[0], self.cara_na[1], self.cara_na[2] = aux

			case Color.VERDE:
				cara[0], cara[1], cara[2], cara[3], cara[5], cara[6], cara[7], cara[8] = cara[6], cara[3], cara[0], cara[7], cara[1], cara[8], cara[5], cara[2]

				aux = self.cara_bl[6], self.cara_bl[7], self.cara_bl[8]
				self.cara_bl[6], self.cara_bl[7], self.cara_bl[8] = self.cara_na[8], self.cara_na[5], self.cara_na[2]
				self.cara_na[8], self.cara_na[5], self.cara_na[2] = self.cara_am[2], self.cara_am[1], self.cara_am[0]
				self.cara_am[2], self.cara_am[1], self.cara_am[0] = self.cara_ro[0], self.cara_ro[3], self.cara_ro[6]
				self.cara_ro[0], self.cara_ro[3], self.cara_ro[6] = aux



				



	def hacer_movimiento(self, movimiento):
		transformacion = self.get_transformacion(movimiento)
		cara, sentido = transformacion
		self.girar(cara, sentido)

	def __str__(self):
		return (
			                                             f"       {self.cara_bl[0]}{self.cara_bl[1]}{self.cara_bl[2]}\n"
			                                             f"       {self.cara_bl[3]}{self.cara_bl[4]}{self.cara_bl[5]}\n"
			                                             f"       {self.cara_bl[6]}{self.cara_bl[7]}{self.cara_bl[8]}\n"
			f"{self.cara_na[0]}{self.cara_na[1]}{self.cara_na[2]} {self.cara_ve[0]}{self.cara_ve[1]}{self.cara_ve[2]} {self.cara_ro[0]}{self.cara_ro[1]}{self.cara_ro[2]} {self.cara_az[0]}{self.cara_az[1]}{self.cara_az[2]}\n"
			f"{self.cara_na[3]}{self.cara_na[4]}{self.cara_na[5]} {self.cara_ve[3]}{self.cara_ve[4]}{self.cara_ve[5]} {self.cara_ro[3]}{self.cara_ro[4]}{self.cara_ro[5]} {self.cara_az[3]}{self.cara_az[4]}{self.cara_az[5]}\n"
			f"{self.cara_na[6]}{self.cara_na[7]}{self.cara_na[8]} {self.cara_ve[6]}{self.cara_ve[7]}{self.cara_ve[8]} {self.cara_ro[6]}{self.cara_ro[7]}{self.cara_ro[8]} {self.cara_az[6]}{self.cara_az[7]}{self.cara_az[8]}\n"
			                                             f"       {self.cara_am[0]}{self.cara_am[1]}{self.cara_am[2]}\n"
			                                             f"       {self.cara_am[3]}{self.cara_am[4]}{self.cara_am[5]}\n"
			                                             f"       {self.cara_am[6]}{self.cara_am[7]}{self.cara_am[8]}\n"
		)

	def __repr__(self):
		return self.__str__()



# class Cara:
# 	def __init__(self, color):
# 		pass


class Color(Enum):
	BLANCO = "bl"
	NARANJA = "na"
	VERDE = "ve"
	ROJO = "ro"
	AZUL = "az"
	AMARILLO = "am"

	def __str__(self):
		return self.value

	def __repr__(self):
		return self.__str__()


if __name__ == '__main__':
	cubo = Cubo()
	print(cubo)
	cubo.hacer_movimiento("R")
	print()
	print(cubo)
	cubo.hacer_movimiento("U")
	print()
	print(cubo)
	cubo.hacer_movimiento("F")
	print()
	print(cubo)
