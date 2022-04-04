import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

size = (500, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pong")

paddle_left = Paddle(0, size[1]/2, size)
paddle_right = Paddle(size[0]-20, size[1]/3, size)
ball = Ball(size[0]/2, size[1]/2, (0, 255, 0), size)

run = True
while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        run = False

    if keys[pygame.K_w]:
        paddle_left.move_up()

    if keys[pygame.K_s]:
        paddle_left.move_down()

    if keys[pygame.K_UP]:
        paddle_right.move_up()

    if keys[pygame.K_DOWN]:
        paddle_right.move_down()

    ball.move(paddle_left, paddle_right)

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 255, 255), (paddle_left.x, paddle_left.y, paddle_left.width, paddle_left.height))
    
    pygame.draw.rect(screen, (255, 255, 255), (paddle_right.x, paddle_right.y, paddle_right.width, paddle_right.height))

    pygame.draw.circle(screen, ball.color, (ball.x, ball.y), ball.radius)

    pygame.display.update()

pygame.quit()