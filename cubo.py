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

		self.can_rotaciones = {
			Color.BLANCO: 0,
			Color.NARANJA: 0,
			Color.VERDE: 0,
			Color.ROJO: 0,
			Color.AZUL: 0,
			Color.AMARILLO: 0
		}

		self.lista_movimientos = []
		
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

		self.lista_movimientos.append(movimiento)

	def mezclar(self, mezcla):
		for mov in mezcla.split(" "):
			self.hacer_movimiento(mov)
			if "2" in mov:
				self.hacer_movimiento(mov)

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
					self.cara_bl.set_linea("U", self.cara_ro.get_linea("R"))
					self.cara_ro.set_linea("R", self.cara_am.get_linea("D'"))
					self.cara_am.set_linea("D'", self.cara_na.get_linea("L'"))
					self.cara_na.set_linea("L'", aux)
				else:
					aux = self.cara_bl.get_linea("U")
					self.cara_bl.set_linea("U", self.cara_na.get_linea("L'"))
					self.cara_na.set_linea("L'", self.cara_am.get_linea("D'"))
					self.cara_am.set_linea("D'", self.cara_ro.get_linea("R"))
					self.cara_ro.set_linea("R", aux)

	def rotar(self, movimiento, prima):
		match movimiento:
			case "X":
				if not prima:
					# rotación visual (tiene que ir antes para que se sume bien en el mapeo)
					self.can_rotaciones[self.posiciones[0].color] += 2 # blanco
					self.can_rotaciones[self.posiciones[4].color] += 2 # azul
					self.can_rotaciones[self.posiciones[3].color] += 1 # rojo
					self.can_rotaciones[self.posiciones[1].color] += 3 # naranja
					# rotación funcional
					self.posiciones[0], self.posiciones[2], self.posiciones[4], self.posiciones[5] = self.posiciones[2], self.posiciones[5], self.posiciones[0], self.posiciones[4]
				else:
					self.can_rotaciones[self.posiciones[5].color] += 2 # amarillo
					self.can_rotaciones[self.posiciones[4].color] += 2 # azul
					self.can_rotaciones[self.posiciones[3].color] += 3 # rojo
					self.can_rotaciones[self.posiciones[1].color] += 1 # naranja
					self.posiciones[2], self.posiciones[5], self.posiciones[0], self.posiciones[4] = self.posiciones[0], self.posiciones[2], self.posiciones[4], self.posiciones[5]
			case "Y":
				if not prima:
					self.can_rotaciones[self.posiciones[0].color] += 1 # blanco
					self.can_rotaciones[self.posiciones[5].color] += 3 # amarillo
					self.posiciones[1], self.posiciones[2], self.posiciones[3], self.posiciones[4] = self.posiciones[2], self.posiciones[3], self.posiciones[4], self.posiciones[1]
				else:
					self.can_rotaciones[self.posiciones[0].color] += 3 # blanco
					self.can_rotaciones[self.posiciones[5].color] += 1 # amarillo
					self.posiciones[2], self.posiciones[3], self.posiciones[4], self.posiciones[1] = self.posiciones[1], self.posiciones[2], self.posiciones[3], self.posiciones[4]
			case "Z":
				if not prima:
					self.can_rotaciones[self.posiciones[0].color] += 1 # blanco
					self.can_rotaciones[self.posiciones[2].color] += 1 # verde
					self.can_rotaciones[self.posiciones[4].color] += 3 # azul
					self.can_rotaciones[self.posiciones[3].color] += 1 # rojo
					self.can_rotaciones[self.posiciones[1].color] += 1 # naranja
					self.can_rotaciones[self.posiciones[5].color] += 1 # amarillo
					self.posiciones[0], self.posiciones[1], self.posiciones[3], self.posiciones[5] = self.posiciones[1], self.posiciones[5], self.posiciones[0], self.posiciones[3]
				else:
					self.can_rotaciones[self.posiciones[0].color] += 3 # blanco
					self.can_rotaciones[self.posiciones[2].color] += 3 # verde
					self.can_rotaciones[self.posiciones[4].color] += 1 # azul
					self.can_rotaciones[self.posiciones[3].color] += 3 # rojo
					self.can_rotaciones[self.posiciones[1].color] += 3 # naranja
					self.can_rotaciones[self.posiciones[5].color] += 3 # amarillo
					self.posiciones[1], self.posiciones[5], self.posiciones[0], self.posiciones[3] = self.posiciones[0], self.posiciones[1], self.posiciones[3], self.posiciones[5]

	def get_posiciones_visual(self):
		posiciones_visual = [Cara(cara.color, cara.cara.copy()) for cara in self.posiciones]
		
		for cara in posiciones_visual:
			for _ in range(self.can_rotaciones[cara.color]):
				cara.rotar()

		return posiciones_visual

	def __str__(self):
		posiciones_visual = self.get_posiciones_visual()

		return (
			                     f"       {posiciones_visual[0][0:3]}\n"
			                     f"       {posiciones_visual[0][3:6]}\n"
			                     f"       {posiciones_visual[0][6: ]}\n"
			f"{posiciones_visual[1][0:3]} {posiciones_visual[2][0:3]} {posiciones_visual[3][0:3]} {posiciones_visual[4][0:3]}\n"
			f"{posiciones_visual[1][3:6]} {posiciones_visual[2][3:6]} {posiciones_visual[3][3:6]} {posiciones_visual[4][3:6]}\n"
			f"{posiciones_visual[1][6: ]} {posiciones_visual[2][6: ]} {posiciones_visual[3][6: ]} {posiciones_visual[4][6: ]}\n"
			                     f"       {posiciones_visual[5][0:3]}\n"
			                     f"       {posiciones_visual[5][3:6]}\n"
			                     f"       {posiciones_visual[5][6: ]}\n"
		)

	def __repr__(self):
		return self.__str__()

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

class Cara:
	def __init__(self, color: Color, cara=None):
		self.color = color
		self.cara = [color] * 9 if cara is None else cara  # renombrar por self.colores
		# 0 1 2
		# 3 4 5
		# 6 7 8

	def __getitem__(self, indice):
		if isinstance(indice, slice):
			parte = self.cara[indice]
			return "".join(str(e) for e in parte)

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

	def __str__(self):
		return "[" + ", ".join(str(c) for c in self.cara) + "]"

	def __repr__(self):
		return self.__str__()


if __name__ == '__main__':
	cubo = Cubo()
	print(cubo)

	mezcla = "U R' F B R2 D' R D2 R2 U2 F' L2 F' B2 D2 R2 F R2 U' B2"
	print(mezcla)
	cubo.mezclar(mezcla)

	mov = input("> ")
	while mov not in  ("Q", "q"):
		cubo.hacer_movimiento(mov)

		print()
		# print(cubo)

		mov = input("> ")
	