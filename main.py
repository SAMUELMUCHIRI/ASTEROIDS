import pygame
from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt=0
    X=SCREEN_WIDTH/2
    Y=SCREEN_HEIGHT/2
    
    player=Player(X, Y)
    updatable = pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)
    Player.containers = (updatable, drawable)
    
    while  True :
        updatable.update(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))  # Fill the screen with black
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()
        dt=(clock.tick(60)/1000 ) # Control the frame rate


if __name__ == "__main__":
    main()


	
