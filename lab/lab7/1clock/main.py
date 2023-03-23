import pygame
import datetime
pygame.init()
W, H = 800, 800
x = W//2
y = H//2
WHITE = (255, 255, 255)
sc = pygame.display.set_mode((W, H))

mickey = pygame.image.load("images/main-clock.png")
leftHand = pygame.image.load("images/left-hand.png")
rightHand = pygame.image.load("images/right-hand.png")
mickeyRect = mickey.get_rect()
def blitRotateCenter(surf, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = center).center)
    surf.blit(rotated_image, new_rect)
langle = 0
rangle = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    t = datetime.datetime.now()  
    minute = int(t.strftime('%M'))*6 -90
    second = int(t.strftime('%S'))*6 -90
    
    sc.fill(WHITE)
    sc.blit(mickey, (x, y))
    sc.blit(mickey, mickeyRect)
    
    blitRotateCenter(sc, leftHand, (x,y), -second) 
    blitRotateCenter(sc, rightHand, (x,y), -minute)
    pygame.display.update()