from enum import Enum

class Cubo:
	def __init__(self):
		self.cara_bl = Cara(Color.BLANCO)
		self.cara_na = Cara(Color.NARANJA)
		self.cara_ve = Cara(Color.VERDE)
		self.cara_ro = Cara(Color.ROJO)
		self.cara_az = Cara(Color.AZUL)
		self.cara_am = Cara(Color.AMARILLO)

		# default: F: verde, U: blanco, R: rojo, ...
		self.posiciones = [self.cara_bl, 
			 self.cara_na, self.cara_ve, self.cara_ro, self.cara_az, 
				  		   self.cara_am]

		self.giros = ("R", "U", "F", "D", "L", "B")
		self.rotaciones = ("X", "Y", "Z")
		
	def hacer_movimiento(self, movimiento):
		movimiento = movimiento.upper()

		if movimiento[0] in self.giros:
			match movimiento[0]:
				case "R":
					cara = self.posiciones[3]
				case "U":
					cara = self.posiciones[0]
				case "F":
					cara = self.posiciones[2]
				case "D":
					cara = self.posiciones[5]
				case "L":
					cara = self.posiciones[1]
				case "B":
					cara = self.posiciones[4]

			prima = "'" in movimiento
			self.girar(cara, prima)

		elif movimiento[0] in self.rotaciones:
			mov = movimiento[0]
			prima = "'" in movimiento
			self.rotar(mov, prima)

	def girar(self, cara, prima=False):
		cara.rotar(prima)
		match cara.color:
			case Color.ROJO:
				if not prima:
					aux = self.cara_ve.get_linea("R")
					self.cara_ve.set_linea("R", self.cara_am.get_linea("R"))
					self.cara_am.set_linea("R", self.cara_az.get_linea("L'"))
					self.cara_az.set_linea("L'", self.cara_bl.get_linea("R"))
					self.cara_bl.set_linea("R", aux)
				else:
					aux = self.cara_ve.get_linea("R")
					self.cara_ve.set_linea("R", self.cara_bl.get_linea("R"))
					self.cara_bl.set_linea("R", self.cara_az.get_linea("L'"))
					self.cara_az.set_linea("L'", self.cara_am.get_linea("R"))
					self.cara_am.set_linea("R", aux)

			case Color.BLANCO:
				if not prima:
					aux = self.cara_ve.get_linea("U")
					self.cara_ve.set_linea("U", self.cara_ro.get_linea("U"))
					self.cara_ro.set_linea("U", self.cara_az.get_linea("U"))
					self.cara_az.set_linea("U", self.cara_na.get_linea("U"))
					self.cara_na.set_linea("U", aux)
				else:
					aux = self.cara_ve.get_linea("U")
					self.cara_ve.set_linea("U", self.cara_na.get_linea("U"))
					self.cara_na.set_linea("U", self.cara_az.get_linea("U"))
					self.cara_az.set_linea("U", self.cara_ro.get_linea("U"))
					self.cara_ro.set_linea("U", aux)

			case Color.VERDE:
				if not prima:
					aux = self.cara_bl.get_linea("D")
					self.cara_bl.set_linea("D", self.cara_na.get_linea("R'"))
					self.cara_na.set_linea("R'", self.cara_am.get_linea("U'"))
					self.cara_am.set_linea("U'", self.cara_ro.get_linea("L"))
					self.cara_ro.set_linea("L", aux)
				else:
					aux = self.cara_bl.get_linea("D")
					self.cara_bl.set_linea("D", self.cara_ro.get_linea("L"))
					self.cara_ro.set_linea("L", self.cara_am.get_linea("U'"))
					self.cara_am.set_linea("U'", self.cara_na.get_linea("R'"))
					self.cara_na.set_linea("R'", aux)

			case Color.AMARILLO:
				if not prima:
					aux = self.cara_ve.get_linea("D")
					self.cara_ve.set_linea("D", self.cara_na.get_linea("D"))
					self.cara_na.set_linea("D", self.cara_az.get_linea("D"))
					self.cara_az.set_linea("D", self.cara_ro.get_linea("D"))
					self.cara_ro.set_linea("D", aux)
				else:
					aux = self.cara_ve.get_linea("D")
					self.cara_ve.set_linea("D", self.cara_ro.get_linea("D"))
					self.cara_ro.set_linea("D", self.cara_az.get_linea("D"))
					self.cara_az.set_linea("D", self.cara_na.get_linea("D"))
					self.cara_na.set_linea("D", aux)

			case Color.NARANJA:
				if not prima:
					aux = self.cara_ve.get_linea("L")
					self.cara_ve.set_linea("L", self.cara_bl.get_linea("L"))
					self.cara_bl.set_linea("L", self.cara_az.get_linea("R'"))
					self.cara_az.set_linea("R'", self.cara_am.get_linea("L"))
					self.cara_am.set_linea("L", aux)
				else:
					aux = self.cara_ve.get_linea("L")
					self.cara_ve.set_linea("L", self.cara_am.get_linea("L"))
					self.cara_am.set_linea("L", self.cara_az.get_linea("R'"))
					self.cara_az.set_linea("R'", self.cara_bl.get_linea("L"))
					self.cara_bl.set_linea("L", aux)

			case Color.AZUL:
				if not prima:
					aux = self.cara_bl.get_linea("U")
					self.cara_bl.set_linea("U", self.cara_ro.get_linea("R'"))
					self.cara_ro.set_linea("R'", self.cara_am.get_linea("D'"))
					self.cara_am.set_linea("D'", self.cara_na.get_linea("L'"))
					self.cara_na.set_linea("L'", aux)
				else:
					aux = self.cara_bl.get_linea("U")
					self.cara_bl.set_linea("U", self.cara_na.get_linea("L'"))
					self.cara_na.set_linea("L'", self.cara_am.get_linea("D'"))
					self.cara_am.set_linea("D'", self.cara_ro.get_linea("R'"))
					self.cara_ro.set_linea("R'", aux)

	def rotar(self, movimiento, prima):
		match movimiento:
			case "X":
				if not prima:
					# rotación funcional
					self.posiciones[0], self.posiciones[2], self.posiciones[4], self.posiciones[5] = self.posiciones[2], self.posiciones[5], self.posiciones[0], self.posiciones[4]
					# rotación visual

				else:
					self.posiciones[2], self.posiciones[5], self.posiciones[0], self.posiciones[4] = self.posiciones[0], self.posiciones[2], self.posiciones[4], self.posiciones[5]
			case "Y":
				if not prima:
					self.posiciones[1], self.posiciones[2], self.posiciones[3], self.posiciones[4] = self.posiciones[2], self.posiciones[3], self.posiciones[4], self.posiciones[1]
				else:
					self.posiciones[2], self.posiciones[3], self.posiciones[4], self.posiciones[1] = self.posiciones[1], self.posiciones[2], self.posiciones[3], self.posiciones[4]
			case "Z":
				if not prima:
					self.posiciones[0], self.posiciones[1], self.posiciones[3], self.posiciones[5] = self.posiciones[1], self.posiciones[5], self.posiciones[0], self.posiciones[3]
				else:
					self.posiciones[1], self.posiciones[5], self.posiciones[0], self.posiciones[3] = self.posiciones[0], self.posiciones[1], self.posiciones[3], self.posiciones[5]

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


class Cara:
	def __init__(self, color: Color):
		self.color = color
		self.cara = [color] * 9		
		# 0 1 2
		# 3 4 5
		# 6 7 8

	def __getitem__(self, indice):
		return self.cara[indice]

	def __setitem__(self, indice, valor):
		self.cara[indice] = valor

	def rotar(self, prima=False):
		if not prima:
			self.cara[0], self.cara[1], self.cara[2], self.cara[3], self.cara[5], self.cara[6], self.cara[7], self.cara[8] = self.cara[6], self.cara[3], self.cara[0], self.cara[7], self.cara[1], self.cara[8], self.cara[5], self.cara[2]
		else:
			self.cara[6], self.cara[3], self.cara[0], self.cara[7], self.cara[1], self.cara[8], self.cara[5], self.cara[2] = self.cara[0], self.cara[1], self.cara[2], self.cara[3], self.cara[5], self.cara[6], self.cara[7], self.cara[8]

	def get_linea(self, linea):
		# líneas: U  D  L  R  - de izquierda a derecha, de arriba hacia abajo
		# líneas: U' D' L' R' - de derecha a izquierda, de abajo hacia arriba
		match linea[0]:
			case "U":
				valores = self.cara[0], self.cara[1], self.cara[2]
			case "D":
				valores = self.cara[6], self.cara[7], self.cara[8]
			case "L":
				valores = self.cara[0], self.cara[3], self.cara[6]
			case "R":
				valores = self.cara[2], self.cara[5], self.cara[8]
		
		return valores if "'" not in linea else valores[::-1]

	def set_linea(self, linea, valores):
		if "'" in linea:
			valores = valores[::-1]
		match linea[0]:
			case "U":
				self.cara[0], self.cara[1], self.cara[2] = valores
			case "D":
				self.cara[6], self.cara[7], self.cara[8] = valores
			case "L":
				self.cara[0], self.cara[3], self.cara[6] = valores
			case "R":
				self.cara[2], self.cara[5], self.cara[8] = valores


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

	mov = input("> ")
	while mov not in  ("Q", "q"):

		cubo.hacer_movimiento(mov)

		print()
		print(cubo)

		mov = input("> ")
	