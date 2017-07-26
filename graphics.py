import pygame

white = ( 255, 255, 255)

main_dis_w = 700
main_dis_h = 400


class Window():
	def __init__(self):
		self.surf = pygame.display.set_mode((main_dis_w, main_dis_h), pygame.FULLSCREEN | pygame.HWSURFACE)
	def redraw(self):
		self.surf.fill(white)
		pygame.display.flip()

class Entity():
	u"Any drowable entity"
	def draw(screen_x, screen_y):
		pass

class Character(Entity):
	"""Mob, NPC or Player"""
	def __init__(self, controller, x, y, speed, hp, direction = 0):
		self.x = x
		self.y = y
		self.speed = speed
		self.hp = hp
		self.brain = controller
		self.direction = direction

	def decide(self):

		dx, dy, self.direction, action = brain.decide()
		x += dx * self.speed
		y += dy * self.speed