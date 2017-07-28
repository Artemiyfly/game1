import pygame
import random
import math
import graphics
import controller

pygame.init()

window = graphics.Window()
#button = graphics.Button()
clock = pygame.time.Clock()


mineLoop = True
while mineLoop:
	last_events = pygame.event.get()
	for event in last_events:
		if event.type == pygame.QUIT:
			mineLoop = False
		if event.type == pygame.KEYDOWN:
			if event.key == controller.K_ESCAPE:
				mineLoop = False
	window.redraw(last_events	)
	#screen.blit(menu1, [0,0])
	window.redraw(last_events)
	clock.tick(60)
	
pygame.quit()
