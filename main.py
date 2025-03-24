import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shoot import *

def main():
    pygame.init()
    game_clock = pygame.time.Clock()            #creates new Clock object
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    #sets screen up
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    score = 0
    life_count = 3
    updatable = pygame.sprite.Group()           #group for updatable thing
    drawable = pygame.sprite.Group()            #group for drawable things
    asteroids = pygame.sprite.Group()           #group for asteroids
    shots = pygame.sprite.Group()
    bursts = pygame.sprite.Group()
    Burst.containers = (updatable, drawable, bursts)
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable)      #asteroid field is only updatable
    Asteroid.containers = (asteroids, updatable, drawable)           #adds all asteroid to these groups
    Player.containers = (updatable, drawable)   #adds all players to updatable and drawable groups
    asteroid_field_1 = AsteroidField()          #creates asteroid field object
    player1 = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))   #sets up player object 
    while True:                                 #infinite while loop keeps game on
        for event in pygame.event.get():        #this for loop makes the close button work
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "black")    #constantly keeps screen black
        for draws in drawable:
            draws.draw(screen)                  #draws all drawables every frame
        updatable.update(dt)                    #updates all updatables every frame
        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid) == True:
                    shot.kill()
                    asteroid.explode()
                    score += 1
            if player1.check_collision(asteroid) == True:
                life_count -= 1
                player1.position.x = SCREEN_WIDTH / 2
                player1.position.y = SCREEN_HEIGHT / 2
                if life_count == 0:
                    print(f"Game over! Your Score was {score}")
                    sys.exit(0)
        pygame.display.flip()                   #refreshes display
        game_clock.tick(60)                     #caps game at 60fps
        dt = game_clock.get_time() / 1000       #returns time between ticks in seconds to dt
        

if __name__ == "__main__":
    main()