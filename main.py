import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from logger import log_state, log_event
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids...")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")    

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    # Initialize clock and dt before the game loop
    clock = pygame.time.Clock()
    dt = 0.0

    # Create the sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    my_group = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Tell the Player class which groups it belongs to automatically
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)


    # Instantiate the Player in the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Game loop starts here
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all objects in the updatable group
        updatable.update(dt)


        # Check if an asteroid hits the player
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
                
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                
        log_state()
        
        # Clear the screen
        screen.fill("black")

        # Draw all objects in the drawable group (including your player)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # Limit framerate to 60 FPS and calculate delta time
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

