import pygame
import random
import math
import graphics

pygame.init()

window = graphics.Window()
window.c()

clock = pygame.time.Clock()

mineLoop = True
while mineLoop:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		mineLoop = False

        screen.fill(white)

        pygame.display(flip)
	clock.tick(40)
	
