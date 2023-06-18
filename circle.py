import pygame 
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height()/ 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('red')
    pygame.draw.circle(screen, 'blue', player_pos, 40)
    pygame.draw.circle (screen, 'green', pygame.mouse.get_pos(),20)

    keys = pygame.key.get_pressed()
    if  keys[pygame.K_w]:
        player_pos.y -= 300 * dt 
    if  keys[pygame.K_s]:
        player_pos.y += 300 * dt 
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt 
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt 
    if player_pos.y <0:
        player_pos.y = 720
    if player_pos.y >720:
        player_pos.y = 0
    if player_pos.x <0:
        player_pos.x = 1280
    if player_pos.x >1280:
        player_pos.x = 0

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    


    #render your game here
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()