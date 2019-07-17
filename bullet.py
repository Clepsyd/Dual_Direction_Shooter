import pygame

radius = 4

class Bullet: 

    def __init__(self, window, x, y, direction, vel):

        self.radius = radius
        self.x = x
        self.y = y
        self.direction = direction
        self.color = pygame.Color(180, 180, 255)
        self.vel = vel

        self.window = window
        self.win_width = window.get_width()
        self.win_height = window.get_height()

    def move(self):

        if self.direction == "left":
            self.x -= self.vel
        if self.direction == "right":
            self.x += self.vel
        if self.direction == "up":
            self.y -= self.vel
        if self.direction == "down":
            self.y += self.vel

    def show(self):

        pygame.draw.circle(
            self.window,
            self.color,
            (int(self.x), int(self.y)),
            int(self.radius)
        )

    def is_offscreen(self):

        cases = {
            self.x < - self.radius * 2,
            self.x >= self.win_width - self.radius * 2,
            self.y < - self.radius * 2,
            self.y >= self.win_height
        }

        for _ in cases:
            if _:
                return True
        
        return False
