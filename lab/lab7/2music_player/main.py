import pygame
pygame.init()

num_mus = 0
get_mus = 0

prev_b = pygame.image.load("images/previous.png")
play_b = pygame.image.load("images/play.png")
next_b = pygame.image.load("images/next.png")

music_list = [pygame.mixer.Sound("sounds/Dynamite.mp3"),
            pygame.mixer.Sound("sounds/asylym.mp3"),
            pygame.mixer.Sound("sounds/hikaya.mp3"),
            pygame.mixer.Sound("sounds/poushi.mp3")]

screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Music player")

label = pygame.font.Font('fonts/Roboto-Black.ttf', 30)

name_list = [label.render("Dynamite - BTS", True, (255,255,255)),
            label.render("Asylym - ASHA Prince", True, (255,255,255)),
            label.render("Hikaya - Madmen", True, (255,255,255)),
            label.render("По уши в тебя влюблен - Miyagi & Andy Panda", True, (255,255,255))]

running = True
while running:
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,255), (0, 300, 700, 200))
    screen.blit(prev_b, (210, 370))
    screen.blit(play_b, (315, 370))
    screen.blit(next_b, (410, 370))
    screen.blit(name_list[num_mus], (30,30))
    pygame.display.update()

  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            music_list[num_mus].play()
            get_mus += 1
        elif event.type == pygame.KEYUP and event.key == pygame.K_RCTRL:
            music_list[num_mus].stop()
        elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            music_list[num_mus].stop()
            num_mus +=1
        elif event.type == pygame.KEYUP and event.type == pygame.K_UP:
            pygame.mixer.music.set_volume(5)
        elif event.type == pygame.KEYUP and event.type == pygame.K_DOWN:
            pygame.mixer.music.set_volume(-5)
        

    if num_mus > len(music_list)-1:
        num_mus = 0