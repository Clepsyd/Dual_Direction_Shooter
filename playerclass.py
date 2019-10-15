import pygame
import bullet
from random import randint


class Direction:

    def __init__(self, key, vect, vel=0):

        self.key = key
        self.vect = vect
        self.vel = vel


class Player:

    VEL_DAMP = 0.8

    # Colors
    WHITE = pygame.Color(255, 255, 255)
    RED = pygame.Color(200, 20, 0)

    def __init__(self, window, height=50, width=50, color=RED):
        self.height = height
        self.width = width
        self.x = 500
        self.y = window.get_height() - self.height - 10
        self.color = color

        self.base_vel = 8
        self.vel = 0
        self.inputs = set()

        self.window = window
        self.win_width = window.get_width()
        self.win_height = window.get_height()

        self.directions = {
            "left": Direction(pygame.K_a, ("x", -1)),
            "right": Direction(pygame.K_d, ("x", 1)),
            "up": Direction(pygame.K_w, ("y", -1)),
            "down": Direction(pygame.K_s, ("y", 1))
        }

        # shooting attributes

        self.shot_vel = randint(10, 20)
        self.bullets = []
        self.shot_cooldown = 0
        self.shooting = False
        self.ammo = 500

    def update_pos(self):

        self.x += self.directions["left"].vel * self.directions["left"].vect[1]
        self.x += self.directions["right"].vel * self.directions["right"].vect[1]
        self.y += self.directions["up"].vel * self.directions["up"].vect[1]
        self.y += self.directions["down"].vel * self.directions["down"].vect[1]

    def is_on_edge(self, direction):

        edges = {
            "left": self.x <= 0,
            "right": self.x >= self.win_width - self.width,
            "up": self.y <= 0,
            "down": self.y >= self.win_height - self.height
        }

        if edges[direction]:
            return True
        else:
            return False

    def move(self, inputs):

        for d in self.directions:
            if inputs[self.directions[d].key]:
                self.directions[d].vel = self.base_vel
            else:
                self.directions[d].vel *= self.VEL_DAMP
            if self.is_on_edge(d) or 0.5 > self.directions[d].vel > 0:
                self.directions[d].vel = 0

        self.update_pos()

    def shoot(self, inputs):

        shots = {
            "left": {
                "key": pygame.K_LEFT,
                "x": self.x,
                "y": self.y + self.height/2
            },
            "right": {
                "key": pygame.K_RIGHT,
                "x": self.x + self.width,
                "y": self.y + self.height/2
            },
            "up": {
                "key": pygame.K_UP,
                "x": self.x + self.width/2,
                "y": self.y
            },
            "down": {
                "key": pygame.K_DOWN,
                "x": self.x + self.width/2,
                "y": self.y + self.height
            }
        }

        for s in shots:
            # if not self.shot_cooldown:
            if not self.shooting:
                if inputs[shots[s]["key"]]:
                    self.bullets.append(bullet.Bullet(
                        self.window,
                        shots[s]["x"] + bullet.radius,
                        shots[s]["y"] + bullet.radius,
                        s,
                        self.shot_vel,
                    ))
                    self.shooting = True
                    self.ammo -= 1
            elif self.shooting:
                self.shooting = False

    def bullets_update(self):

        for bullet in self.bullets:
            bullet.show()
            bullet.move()
            if bullet.is_offscreen():
                self.bullets.remove(bullet)

    def show(self):
        pygame.draw.rect(
            self.window,
            self.color,
            (self.x, self.y, self.width, self.height)
        )
