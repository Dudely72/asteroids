import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():        #this for loop makes the close button work
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "black")    #constantly keeps screen black
        pygame.display.flip()                   #refreshes display

if __name__ == "__main__":
    main()