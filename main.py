import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from logger import log_state

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

    # Tell the Player class which groups it belongs to automatically
    Player.containers = (updatable, drawable)

    # Instantiate the Player in the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop starts here
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all objects in the updatable group
        updatable.update(dt)
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

