import pygame

white = ( 255, 255, 255)

main_dis_w = 1360
main_dis_h = 768



class Window():
	def __init__(self):
		self.surf = pygame.display.set_mode((main_dis_w, main_dis_h), pygame.FULLSCREEN | pygame.HWSURFACE)
	def redraw(self,last_events):
		self.surf.fill(white)
		'DRAW ALL ENTITIES'
		pygame.display.flip()

class Entity(object):
	"Any drowable entity"
	def __init__(self, x, y, texture, height = -1, width = -1):
		self.x = x
		self.y = y
		self.texture = texture
		if width == -1:
			self.height = texture[0].get_height()
			self.width = texture[0].get_width()
		else:
			self.height = height
			self.width = width
	def update(self, last_events):
		pass
	def draw(screen_x, screen_y):
		if -width < x - screen_x < main_dis_w and -height < y - screen_y < main_dis_h:
			screen.blit(texture[0], (x - screen_x, y - screen_y))

class Character(Entity):
	"Mob, NPC or Player"
	def __init__(self, controller, x, y, texture, speed, hp, direction = 0):
		super(Character, self).__init__(x, y, texture)
		self.speed = speed
		self.hp = hp
		self.brain = controller
		self.direction = direction

	def update(self, last_events):
		dx, dy, self.direction, action = brain.decide(last_events)
		x += dx * self.speed
		y += dy * self.speed
		'HANDLE DIRECTION AND ACTION'
	def draw(screen_x, screen_y):
		"CHARACTERS ARE DRAWEN DIFFERENTLY"
		pass

class Button(Entity):
        def __init__(self, x, y, texture, func):
                super(Button, self).__init__(x,y,texture)
                self.selected = False
                self.func = func
		def update(self, last_events):
			mouse_pos = pygame.mouse.get_pos()
			mouse_x = mouse_pos[0]
			mouse_y = mouse_pos[1]
			self.selected = mouse_x > x and mouse_x < x+width and mouse_y > y and mouse_y < y+height
		def draw(screen_x, screen_y):
			if self.selected:
				screen.blit(texture[1], [x, y])
			else:
				screen.blit(texture[0], [x, y])
