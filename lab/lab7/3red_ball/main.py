import pygame
pygame.init()

clock = pygame.time.Clock()

W , H = 564, 360
ball_x = W/2
ball_y = H/2

screen = pygame.display.set_mode((W, H))
background = pygame.image.load("images/footballfield.jpg").convert_alpha()

running = True
while running:
    clock.tick(30)
    

    keys= pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and ball_x < W - 60:
            ball_x += 20
    elif keys[pygame.K_LEFT] and ball_x > 60:
        ball_x -= 20
    elif keys[pygame.K_DOWN] and ball_y < H-40:
        ball_y += 20
    elif keys[pygame.K_UP] and ball_y > 40:
        ball_y -= 20 

    screen.blit(background,(0,0))
    pygame.draw.circle(screen, ("Red"), (ball_x, ball_y), 25)
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()