import pygame

K_UP = pygame.K_w
K_DOWN = pygame.K_s
K_LEFT = pygame.K_a
K_RIGHT = pygame.K_d
K_ESCAPE = pygame.K_ESCAPE

class Player():
    def __init__(self):
        self.h_y_speed = 0
        self.h_y_speed = 0
    def decide(self, last_events):
        'ALSO NEED TO GET ALL ENTITIES'
        for event in last_events:
            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    self.h_y_speed = -1
                if event.key == K_DOWN:
                    self.h_y_speed = 1
                if event.key == K_LEFT:
                    self.h_x_speed = -1
                if event.key == K_RIGHT:
                    self.h_y_speed = 1
            if event.type == pygame.KEYUP:
                if event.key == K_UP:
                    self.h_y_speed = 0
                if event.key == K_DOWN:
                    self.h_y_speed = 0
                if event.key == K_LEFT:
                    self.h_x_speed = 0
                if event.key == K_RIGHT:
                    self.h_y_speed = 0
        "GET DIRECTION AND ACTION"
        return self.h_x_speed, self.h_y_speed, 0, None
