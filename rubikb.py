import pygame

pygame.init()

screen = pygame.display.set_mode((512, 512))

running = True
while running:

	r = pygame.Rect(10, 10, 100, 100)

	pygame.draw.rect(screen, (128, 128, 255), r)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.flip()

pygame.quit()
