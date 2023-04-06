import pygame, random, time
pygame.init()
FPS = pygame.time.Clock()

#Screen information
W, H = 400, 600
SPEED = 5
coin_y = 0
SCORE = 0
screen = pygame.display.set_mode((W, H))
screen.fill((255, 255, 255))
pygame.display.set_caption("Game") 

#Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, (0,0,0))

#Background

background = pygame.image.load("images/AnimatedStreet.png")

#Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global coin_y
        self.image = pygame.image.load("images/coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 700 or pygame.sprite.spritecollideany(P1, enemies):
            if pygame.sprite.spritecollideany(P1, enemies):
                SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, W-40),0)

#PLayer
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image =  pygame.image.load("images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    def move(self):
        keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < W:
            if keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)

#Setting up Sprites
E1 = Enemy()
P1 = Player()
b_y=0

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)

#Adding a new User event
# INC_SPEED = pygame.USEREVENT + 1
# pygame.time.set_timer(INC_SPEED, 1000)

pygame.mixer.Sound("sounds/background.wav").play(1000)

#Game loop
running = True
while running:
    for event in pygame.event.get():
        # if event.type == INC_SPEED:
        #     SPEED +=0.5

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    screen.blit(background, (0,b_y))
    screen.blit(background, (0,b_y-600))
    scores = font_small.render(str(SCORE), True, (0,0,0))
    screen.blit(scores, (10,10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    #To be run if collision occurs between Player and Enemy
    # if pygame.sprite.spritecollideany(P1, enemies):


        #   pygame.display.update()
        #   for entity in all_sprites:
        #       entity.kill() 
        #   time.sleep(2)
        #   pygame.quit()
    b_y+=5

    if b_y > 600:
        b_y = 0
    pygame.display.flip()
    FPS.tick(60)