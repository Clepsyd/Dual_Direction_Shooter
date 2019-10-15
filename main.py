import pygame
import playerclass
import enemy
from random import randint

pygame.init()
window_height = 900
window_width = 1600
window = pygame.display.set_mode((window_width, window_height))

score = 0
game_over = False

# objects
player = playerclass.Player(window)
targets = []
countdown_len = randint(150, 190)
target_countdown = countdown_len

run = True
clock = pygame.time.Clock()
framerate = 60
water_font = pygame.font.Font("Righteous-Regular.ttf", 48)
score_font = pygame.font.Font("Righteous-Regular.ttf", 100)

while run:

    window.fill((0, 15, 0))
    clock.tick(framerate)

    inputs = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player.move(inputs)
    player.show()
    player.shoot(inputs)
    player.shot_vel = randint(10,20)
    player.bullets_update()
    water_text = water_font.render(
            f"Water: {player.ammo}",
            False,
            (255, 255, 255)
        )
    window.blit(water_text, (10, 10))


    if target_countdown == 0:
        # if len(targets):
        #     targets.pop()
        targets.append(enemy.Enemy(
            window,
            50,
            50,
            randint(0, window_width - 50),
            randint(0, window_height - 50)
        ))
        target_countdown = countdown_len
    target_countdown -= 1

    for target in targets:
        target.show()
        target.check_hit(player.bullets)
        if target.hp == 0:
            targets.remove(target)
            score += 10

    pygame.display.flip()

    if not player.ammo or len(targets) > 3:
        run = False
        game_over = True
        # font = pygame.font.Font("Righteous-Regular.ttf", 54)
        score_text = score_font.render(
            f"YOUR SCORE: {score}",
            False,
            (255, 255, 255)
        )
        window.fill((0, 0, 0))
        window.blit(score_text, (window_width/2 - 100, window_height/2))
        pygame.display.flip()


# Game Over screen

while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False


pygame.quit()
