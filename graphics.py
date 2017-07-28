dimport pygame

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
        def __init__(self, x, y):
                super(Button, self).__init__(x, y, texture)

        def draw(screen_x, screen_y):
                pass
        def __init__(self, x, y, texture):
                super(Button, self).__init__(x,y,texture)
                self.texture = texture
        def draw(screen_x, screen_y):
                screen.blit(texture, [x, y])
