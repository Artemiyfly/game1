import pygame

white = ( 255, 255, 255)

main_dis_w = 700
main_dis_h = 400


class Window():
	def c(this):
		screen = pygame.display.set_mode((main_dis_w, main_dis_h))
	def redraw():
		pass

class Moving():
        def key_mov:
                if event.type == pygame.KEYUP:
                        if event.key = K_UP:
                                h_y_speed = -3
                        if event.key = K_DOWN:
                                h_y_speed = 3
                        if event.key = K_LEFT:
                                h_x_speed = -3
                        if event.key = K_RIGHT:
                                h_y_speed = 3

                if event.type == pygame.KEYDOWN:
                        if event.key = K_UP:
                                h_y_speed = 0
                        if event.key = K_DOWN:
                                h_y_speed = 0
                        if event.key = K_LEFT:
                                h_x_speed = 0
                        if event.key = K_RIGHT:
                                h_y_speed = 0

                h_x_coord = x_coord + h_x_speed
                h_y_coord = y_coord + h+y_speed
                        
