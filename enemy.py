import pygame

RED = pygame.Color(75, 10, 10)
DARK_ORANGE = pygame.Color(100, 50, 25)
LIGHT_ORANGE = pygame.Color(199,81,0)
YELLOW = pygame.Color(255,255,0)
BRIGHT_YELLOW = pygame.Color(255,248,212)

class Enemy:

    def __init__(self, window, height, width, x, y):

        self.window = window
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.color = pygame.Color(255, 255, 255)
        self.basehp = 20
        self.hp = self.basehp

    def show(self):

        if self.hp > 0.8 * self.basehp:
            self.color = BRIGHT_YELLOW
        elif self.hp > 0.6 * self.basehp:
            self.color = YELLOW
        elif self.hp > 0.4 * self.basehp:
            self.color = LIGHT_ORANGE
        elif self.hp > 0.2 * self.basehp:
            self.color = DARK_ORANGE
        else:
            self.color = RED

        pygame.draw.rect(
            self.window,
            self.color,
            (self.x, self.y, self.width, self.height)
        )

    def check_hit(self, bullets):

        for bullet in bullets:
            if (
                self.x - bullet.radius < bullet.x < self.x + self.width + bullet.radius and
                self.y - bullet.radius < bullet.y < self.y + self.height + bullet.radius
            ):
                bullets.remove(bullet)
                self.hp -= 1
                return True
        return False