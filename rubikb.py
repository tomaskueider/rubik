import pygame
from cubo import Cubo, Color

pygame.init()

screen = pygame.display.set_mode((512, 512))
screen.fill((20, 25, 31))

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


cubo = Cubo()
size = 20
running = True
while running:

	# rects con coordenadas
	u0 = pygame.Rect(246, 100, size, size)
	u1 = pygame.Rect(270, 112, size, size)
	u2 = pygame.Rect(294, 124, size, size)
	u3 = pygame.Rect(222, 112, size, size)
	u4 = pygame.Rect(246, 124, size, size)
	u5 = pygame.Rect(270, 136, size, size)
	u6 = pygame.Rect(198, 124, size, size)
	u7 = pygame.Rect(222, 136, size, size)
	u8 = pygame.Rect(246, 148, size, size)

	f0 = pygame.Rect(186, 148, size, size)
	f1 = pygame.Rect(210, 160, size, size)
	f2 = pygame.Rect(234, 172, size, size)
	f3 = pygame.Rect(186, 172, size, size)
	f4 = pygame.Rect(210, 184, size, size)
	f5 = pygame.Rect(234, 196, size, size)
	f6 = pygame.Rect(186, 196, size, size)
	f7 = pygame.Rect(210, 208, size, size)
	f8 = pygame.Rect(234, 220, size, size)

	r0 = pygame.Rect(258, 172, size, size)
	r1 = pygame.Rect(282, 160, size, size)
	r2 = pygame.Rect(306, 148, size, size)
	r3 = pygame.Rect(258, 196, size, size)
	r4 = pygame.Rect(282, 184, size, size)
	r5 = pygame.Rect(306, 172, size, size)
	r6 = pygame.Rect(258, 220, size, size)
	r7 = pygame.Rect(282, 208, size, size)
	r8 = pygame.Rect(306, 196, size, size)

	u = cubo.posiciones[0]
	f = cubo.posiciones[2]
	r = cubo.posiciones[3]

	# definir colores y dibujarlos
	pygame.draw.rect(screen, get_color(u[0]), u0)
	pygame.draw.rect(screen, get_color(u[1]), u1)
	pygame.draw.rect(screen, get_color(u[2]), u2)
	pygame.draw.rect(screen, get_color(u[3]), u3)
	pygame.draw.rect(screen, get_color(u[4]), u4)
	pygame.draw.rect(screen, get_color(u[5]), u5)
	pygame.draw.rect(screen, get_color(u[6]), u6)
	pygame.draw.rect(screen, get_color(u[7]), u7)
	pygame.draw.rect(screen, get_color(u[8]), u8)

	pygame.draw.rect(screen, get_color(f[0]), f0)
	pygame.draw.rect(screen, get_color(f[1]), f1)
	pygame.draw.rect(screen, get_color(f[2]), f2)
	pygame.draw.rect(screen, get_color(f[3]), f3)
	pygame.draw.rect(screen, get_color(f[4]), f4)
	pygame.draw.rect(screen, get_color(f[5]), f5)
	pygame.draw.rect(screen, get_color(f[6]), f6)
	pygame.draw.rect(screen, get_color(f[7]), f7)
	pygame.draw.rect(screen, get_color(f[8]), f8)

	pygame.draw.rect(screen, get_color(r[0]), r0)
	pygame.draw.rect(screen, get_color(r[1]), r1)
	pygame.draw.rect(screen, get_color(r[2]), r2)
	pygame.draw.rect(screen, get_color(r[3]), r3)
	pygame.draw.rect(screen, get_color(r[4]), r4)
	pygame.draw.rect(screen, get_color(r[5]), r5)
	pygame.draw.rect(screen, get_color(r[6]), r6)
	pygame.draw.rect(screen, get_color(r[7]), r7)
	pygame.draw.rect(screen, get_color(r[8]), r8)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.flip()

pygame.quit()
