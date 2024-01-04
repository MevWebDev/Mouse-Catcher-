import pygame, sys
import random
import asyncio
SIZE = 40
# pygame setup
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
flippedx = False
flippedy = False
running = True
clock = pygame.time.Clock()
game_surface = pygame.Surface((1280*0.8, 720*0.8))


player_pos = pygame.math.Vector2(580, 300)


cat_surface = pygame.image.load('src/cat.png')
cat_surface = pygame.transform.scale(cat_surface, (100, 100))

# mouse_surface = pygame.image.load('src/mouse.png')
# mouse_surface = pygame.transform.scale(mouse_surface, (100, 100))

while True:
    screen.fill("pink")
    screen.blit(game_surface, (128,72))
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
            
    screen.blit(cat_surface, (player_pos))
    

                
    

    
  
        

            
    
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if flippedy == True:
            flippedy = False
            cat_surface = pygame.transform.flip(cat_surface, False, True)
        if player_pos.y - 600 * dt > 72:
            player_pos.y -= 600 * dt
    if keys[pygame.K_s]:
        if flippedy == False:
            flippedy = True
            cat_surface = pygame.transform.flip(cat_surface, False, True)
        if player_pos.y + 600 * dt < 648 - 100:  # Subtract the size of the cat to prevent it from going off the bottom edge
            player_pos.y += 600 * dt
    if keys[pygame.K_a]:
        if flippedx == True:
            cat_surface = pygame.transform.flip(cat_surface, True, False)
            flippedx = False
        if player_pos.x - 600 * dt > 128:
            player_pos.x -= 600 * dt
    if keys[pygame.K_d]:
        if flippedx == False:
            flippedx = True
            cat_surface = pygame.transform.flip(cat_surface, True, False)
        if player_pos.x + 600 * dt < 1152 - 100:  # Subtract the size of the cat to prevent it from going off the right edge
            player_pos.x += 600 * dt

    # flip() the display to put your work on screen
    pygame.display.update()

    # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()