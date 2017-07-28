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
			'TODO: GET SIZE OF IMAGE'
			pass
		else:
			self.height = height
			self.width = width
	def draw(screen_x, screen_y):
		'DRAW ENTITY'
		pass

class Character(Entity):
	"Mob, NPC or Player"
	def __init__(self, controller, x, y, texture, speed, hp, direction = 0):
		super(Character, self).__init__(x, y, texture)
		self.speed = speed
		self.hp = hp
		self.brain = controller
		self.direction = direction

	def decide(self, last_events):
		dx, dy, self.direction, action = brain.decide(last_events)
		x += dx * self.speed
		y += dy * self.speed
		'HANDLE DIRECTION AND ACTION'
	def draw(screen_x, screen_y):
		"CHARACTERS ARE DRAWEN DIFFERENTLY"
		pass

class Button(Entity):
        def __init__(self, x, y, texture):
                super(Button, self).__init__(x,y,texture)
        def draw(screen_x, screen_y):
                mouse_pos = pygame.mouse.get_pos()
                mouse_x = mouse_pos[0]
                mouse_y = mouse_pos[1]
                screen.blit(texture[0], [x, y])
                if mouse_x > x and mouse_x < x+width and mouse_y > y and mouse_y < y+height:
                        screen.blit(texture[1], [x, y])
        def update()
