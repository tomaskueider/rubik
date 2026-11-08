import pygame
from cubo import Cubo, Color

pygame.init()

# visibilidad de la parte de atrás del cubo para debug
back = True

## pantalla ##
screen_size = (512, 512) if not back else (1024, 512)
screen_color = (20, 25, 31)
screen = pygame.display.set_mode(screen_size)
screen.fill(screen_color)
##############


## funciones ##
def get_color(color):
	match color:
		case Color.BLANCO:
			return (255, 255, 255)
		case Color.NARANJA:
			return (255, 100, 0)
		case Color.VERDE:
			return (0, 187, 0)
		case Color.ROJO:
			return (255, 0, 0)
		case Color.AZUL:
			return (0, 0, 187)
		case Color.AMARILLO:
			return (255, 255, 0)

# tuplas #
def sumar_tuplas(t1, t2):
	return ((t1[0] + t2[0]), (t1[1] + t2[1]))

def multiplicar_tupla(t, v):
	return ((t[0] * v), (t[1] * v))

def restar_tuplas(t1, t2):
	return ((t1[0] - t2[0]), (t1[1] - t2[1]))

def dividir_tupla(t, v):
	return ((t[0] // v), (t[1] // v))
##########

def get_coords(position, template, size, offset):
	return tuple(sumar_tuplas(multiplicar_tupla(sumar_tuplas(position, template[i]), size), offset) for i in range(4))
	
def get_coords_back(position, template, size, offset):
	coords = list(sumar_tuplas(multiplicar_tupla(sumar_tuplas(position, template[i]), size), offset) for i in range(4))
	despl_coords = tuple((c[0] + 512, c[1]) for c in coords)
	return despl_coords

def get_offset(cube_center, size, screen_size):
	center = multiplicar_tupla(cube_center, size) # radio
	center = multiplicar_tupla(center, 2) # diámetro - esto seguro se puede hacer más limpio
	return tuple(dividir_tupla(restar_tuplas(screen_size, center), 2))
###############


## coords stickers ##
templ_u = ((0, 0), (2, 1), (0, 2), (-2, 1))
templ_f = ((0, 0), (2, 1), (2, 3.33), (0, 2.33))
templ_r = ((0, 0), (2, -1), (2, 1.33), (0, 2.33))

coords_base = {
		"u": ((6, 0), (8, 1), (10, 2), (4, 1), (6, 2), (8, 3), (2, 2), (4, 3), (6, 4)),
		"f": ((0, 3), (2, 4), (4, 5), (0, 5.33), (2, 6.33), (4, 7.33), (0, 7.67), (2, 8.67), (4, 9.67)),
		"r": ((6, 6), (8, 5), (10, 4), (6, 8.33), (8, 7.33), (10, 6.33), (6, 10.67), (8, 9.67), (10, 8.67)),
		# back:
		"d": ((2, 2), (4, 1), (6, 0), (4, 3), (6, 2), (8, 1), (6, 4), (8, 3), (10, 2)), # u - 7, 4, 1, 8, 5, 2, 9, 6, 3
		"l": ((4, 9.67), (2, 8.67), (0, 7.67), (4, 7.33), (2, 6.33), (0, 5.33), (4, 5), (2, 4), (0, 3)), # f - 9, 8, 7, 6, 5, 4, 3, 2, 1
		"b": ((10, 8.67), (8, 9.67), (6, 10.67), (10, 6.33), (8, 7.33), (6, 8.33), (10, 4), (8, 5), (6, 6)) # r - 9, 8, 7, 6, 5, 4, 3, 2, 1
	}
# multiplicar todo x3 (y size /3) para que quede redondo
# lo hice a esta escala para que la distancia más chica quede en 1
#####################


## variables ##
size = 20

# offset (mejorar)
cube_center = coords_base["r"][0]
offset = get_offset(cube_center, size, (512, 512)) # screen_size
#

# bordes
outline_color = (24, 24, 24)
outline_width = size // 5
###############


## inicialización del cubo ##
cubo = Cubo()
mezcla = "U R' F B R2 D' R D2 R2 U2 F' L2 F' B2 D2 R2 F R2 U' B2"
cubo.mezclar(mezcla)
#############################

running = True
while running:
	# colores
	caras = cubo.get_posiciones_visual() # cambiar nombre por colores
	colores_u = caras[0]
	colores_f = caras[2]
	colores_r = caras[3]

	# coords de los stickers
	# esto se puede hacer más limpio
	coords_u = coords_base["u"]
	coords_f = coords_base["f"]
	coords_r = coords_base["r"]

	# dibujado de los stickers
	for color, coords in zip(colores_u, coords_u):
		pygame.draw.polygon(screen, get_color(color), get_coords(coords, templ_u, size, offset))
		pygame.draw.polygon(screen, outline_color, get_coords(coords, templ_u, size, offset), outline_width)
	
	for color, coords in zip(colores_f, coords_f):
		pygame.draw.polygon(screen, get_color(color), get_coords(coords, templ_f, size, offset))
		pygame.draw.polygon(screen, outline_color, get_coords(coords, templ_f, size, offset), outline_width)

	for color, coords in zip(colores_r, coords_r):
		pygame.draw.polygon(screen, get_color(color), get_coords(coords, templ_r, size, offset))
		pygame.draw.polygon(screen, outline_color, get_coords(coords, templ_r, size, offset), outline_width)


	if back:
		colores_d = caras[5]
		colores_b = caras[4]
		colores_l = caras[1]

		coords_d = coords_base["d"]
		coords_b = coords_base["b"]
		coords_l = coords_base["l"]

		for color, coords in zip(colores_d, coords_d):
			pygame.draw.polygon(screen, get_color(color), get_coords_back(coords, templ_u, size, offset))
			pygame.draw.polygon(screen, outline_color, get_coords_back(coords, templ_u, size, offset), outline_width)
		
		for color, coords in zip(colores_b, coords_b):
			pygame.draw.polygon(screen, get_color(color), get_coords_back(coords, templ_r, size, offset))
			pygame.draw.polygon(screen, outline_color, get_coords_back(coords, templ_r, size, offset), outline_width)

		for color, coords in zip(colores_l, coords_l):
			pygame.draw.polygon(screen, get_color(color), get_coords_back(coords, templ_f, size, offset))
			pygame.draw.polygon(screen, outline_color, get_coords_back(coords, templ_f, size, offset), outline_width)


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			match event.key:
				case pygame.K_r: # k
					m = "r"
				case pygame.K_l: # f
					m = "l"
				case pygame.K_u: # u
					m = "u"
				case pygame.K_d: # d
					m = "d"
				case pygame.K_f: # j
					m = "f"
				case pygame.K_b: # i
					m = "b"
				case pygame.K_x: # l
					m = "x"
				case pygame.K_y: # o
					m = "y"
				case pygame.K_x: # s
					m = "z"
				case pygame.K_q: # q
					m = None
					running = False
					print("movimientos: ")
					print(*cubo.lista_movimientos, sep=", ")
				case _:
					break

			if m and event.mod & pygame.KMOD_SHIFT:
				m += "'"

			if m:
				cubo.hacer_movimiento(m)

	pygame.display.flip()

pygame.quit()
