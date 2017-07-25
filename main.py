import pygame
import random
import math
import graphics

pygame.init()

window = graphics.Window()
window.c()

mineLoop = True
while mineLoop:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		mineLoop = False