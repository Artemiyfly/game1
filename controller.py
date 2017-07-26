class Player():
    def __init__(this):
        this.h_y_speed = 0
        this.h_y_speed = 0
    def decide(this, last_events):
        for event in last_events:
            if event.type == pygame.KEYUP:
                if event.key == K_UP:
                    this.h_y_speed = -1
                if event.key == K_DOWN:
                    this.h_y_speed = 1
                if event.key == K_LEFT:
                    this.h_x_speed = -1
                if event.key == K_RIGHT:
                    this.h_y_speed = 1
            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    this.h_y_speed = 0
                if event.key == K_DOWN:
                    this.h_y_speed = 0
                if event.key == K_LEFT:
                    this.h_x_speed = 0
                if event.key == K_RIGHT:
                    this.h_y_speed = 0
        return this.h_x_speed, this.h_y_speed, 0, None