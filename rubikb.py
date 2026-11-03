import pygame

pygame.init()

screen = pygame.display.set_mode((512, 512))
screen.fill((20, 25, 31))

size = 20

running = True
while running:

	a1 = pygame.Rect(246, 100, size, size)
	a2 = pygame.Rect(270, 112, size, size)
	a3 = pygame.Rect(294, 124, size, size)
	a4 = pygame.Rect(222, 112, size, size)
	a5 = pygame.Rect(246, 124, size, size)
	a6 = pygame.Rect(270, 136, size, size)
	a7 = pygame.Rect(198, 124, size, size)
	a8 = pygame.Rect(222, 136, size, size)
	a9 = pygame.Rect(246, 148, size, size)

	b1 = pygame.Rect(186, 148, size, size)
	b2 = pygame.Rect(210, 160, size, size)
	b3 = pygame.Rect(234, 172, size, size)
	b4 = pygame.Rect(186, 172, size, size)
	b5 = pygame.Rect(210, 184, size, size)
	b6 = pygame.Rect(234, 196, size, size)
	b7 = pygame.Rect(186, 196, size, size)
	b8 = pygame.Rect(210, 208, size, size)
	b9 = pygame.Rect(234, 220, size, size)

	c1 = pygame.Rect(258, 172, size, size)
	c2 = pygame.Rect(282, 160, size, size)
	c3 = pygame.Rect(306, 148, size, size)
	c4 = pygame.Rect(258, 196, size, size)
	c5 = pygame.Rect(282, 184, size, size)
	c6 = pygame.Rect(306, 172, size, size)
	c7 = pygame.Rect(258, 220, size, size)
	c8 = pygame.Rect(282, 208, size, size)
	c9 = pygame.Rect(306, 196, size, size)



	pygame.draw.rect(screen, (255, 255, 255), a1)
	pygame.draw.rect(screen, (255, 255, 255), a2)
	pygame.draw.rect(screen, (255, 255, 255), a3)
	pygame.draw.rect(screen, (255, 255, 255), a4)
	pygame.draw.rect(screen, (255, 255, 255), a5)
	pygame.draw.rect(screen, (255, 255, 255), a6)
	pygame.draw.rect(screen, (255, 255, 255), a7)
	pygame.draw.rect(screen, (255, 255, 255), a8)
	pygame.draw.rect(screen, (255, 255, 255), a9)

	pygame.draw.rect(screen, (99, 195, 99), b1)
	pygame.draw.rect(screen, (99, 195, 99), b2)
	pygame.draw.rect(screen, (99, 195, 99), b3)
	pygame.draw.rect(screen, (99, 195, 99), b4)
	pygame.draw.rect(screen, (99, 195, 99), b5)
	pygame.draw.rect(screen, (99, 195, 99), b6)
	pygame.draw.rect(screen, (99, 195, 99), b7)
	pygame.draw.rect(screen, (99, 195, 99), b8)
	pygame.draw.rect(screen, (99, 195, 99), b9)

	pygame.draw.rect(screen, (255, 82, 82), c1)
	pygame.draw.rect(screen, (255, 82, 82), c2)
	pygame.draw.rect(screen, (255, 82, 82), c3)
	pygame.draw.rect(screen, (255, 82, 82), c4)
	pygame.draw.rect(screen, (255, 82, 82), c5)
	pygame.draw.rect(screen, (255, 82, 82), c6)
	pygame.draw.rect(screen, (255, 82, 82), c7)
	pygame.draw.rect(screen, (255, 82, 82), c8)
	pygame.draw.rect(screen, (255, 82, 82), c9)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.flip()

pygame.quit()
